#!/usr/bin/env python3
"""
generate_fee_pdf.py
สร้าง PDF ใบแจ้งชำระเงินค่าซื้อเอกสารประกวดราคาอิเล็กทรอนิกส์

Usage:
    python generate_fee_pdf.py <config.json>

Config JSON fields:
    project_id    : เลขโครงการ e-GP เช่น "69059480871"
    agency_name   : ชื่อหน่วยงานเต็ม เช่น "องค์การบริหารส่วนตำบลหนองโพธิ์"
    agency_short  : ชื่อย่อ เช่น "อบต.หนองโพธิ์"
    amount        : ยอดเงิน (float) เช่น 5000.00
    bank          : ชื่อธนาคาร เช่น "ธนาคารกรุงไทย"
    account_no    : เลขบัญชี เช่น "402-6-02085-1"
    payer_name    : ชื่อผู้ชำระ
    payer_phone   : เบอร์โทร เช่น "087-223-5093"
    slip_path     : path ของไฟล์สลิป (PDF หรือ JPG)
    log_dir       : path ของโฟลเดอร์ E-BIDDING/Log/ (string, แปลงเป็น bytes ใน script)
"""

import json
import os
import sys
import subprocess
import tempfile
import urllib.request
from pathlib import Path


# ─── Dependencies ──────────────────────────────────────────────────────────────

def install_deps():
    pkgs = ['reportlab', 'PyMuPDF', 'Pillow']
    subprocess.run(
        [sys.executable, '-m', 'pip', 'install'] + pkgs +
        ['--break-system-packages', '-q'],
        check=True, capture_output=True
    )


# ─── Fonts ─────────────────────────────────────────────────────────────────────

FONT_DIR = Path('/tmp/sarabun_fonts')
FONTS = {
    'Sarabun-Regular.ttf':
        'https://github.com/google/fonts/raw/main/ofl/sarabun/Sarabun-Regular.ttf',
    'Sarabun-Bold.ttf':
        'https://github.com/google/fonts/raw/main/ofl/sarabun/Sarabun-Bold.ttf',
}

def ensure_fonts() -> Path:
    FONT_DIR.mkdir(exist_ok=True)
    for fname, url in FONTS.items():
        fpath = FONT_DIR / fname
        if not fpath.exists():
            print(f'  Downloading {fname}...')
            urllib.request.urlretrieve(url, fpath)
    return FONT_DIR


# ─── Slip → PNG ────────────────────────────────────────────────────────────────

def slip_to_png(slip_path: str) -> str:
    slip = Path(slip_path)
    out = Path('/tmp') / (slip.stem + '_slip_embed.png')
    suffix = slip.suffix.lower()

    if suffix == '.pdf':
        import fitz  # PyMuPDF
        doc = fitz.open(str(slip))
        page = doc[0]
        mat = fitz.Matrix(2.0, 2.0)  # 2× zoom for print quality
        pix = page.get_pixmap(matrix=mat)
        pix.save(str(out))
        doc.close()
    elif suffix in ('.jpg', '.jpeg', '.png'):
        from PIL import Image
        img = Image.open(str(slip))
        img.save(str(out), 'PNG')
    else:
        raise ValueError(f'Unsupported slip format: {suffix}')

    return str(out)


# ─── Amount → Thai Words ───────────────────────────────────────────────────────

_ONES = ['', 'หนึ่ง', 'สอง', 'สาม', 'สี่', 'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า']
_PLACES = ['', 'สิบ', 'ร้อย', 'พัน', 'หมื่น', 'แสน', 'ล้าน']

def _group_to_words(n: int) -> str:
    if n == 0:
        return ''
    digits = []
    tmp = n
    while tmp > 0:
        digits.append(tmp % 10)
        tmp //= 10
    digits.reverse()
    result = ''
    length = len(digits)
    for i, d in enumerate(digits):
        pos = length - 1 - i
        if d == 0:
            continue
        if pos == 1:  # tens place
            if d == 1:
                result += 'สิบ'
            elif d == 2:
                result += 'ยี่สิบ'
            else:
                result += _ONES[d] + 'สิบ'
        elif pos == 0 and d == 1 and length > 1:
            result += 'เอ็ด'
        else:
            result += _ONES[d] + _PLACES[pos]
    return result

def baht_to_words(amount: float) -> str:
    total_satang = round(amount * 100)
    baht_int = total_satang // 100
    satang = total_satang % 100

    if baht_int >= 1_000_000:
        millions = baht_int // 1_000_000
        remainder = baht_int % 1_000_000
        text = _group_to_words(millions) + 'ล้าน'
        if remainder > 0:
            text += _group_to_words(remainder)
    elif baht_int > 0:
        text = _group_to_words(baht_int)
    else:
        text = 'ศูนย์'

    text += 'บาท'
    text += (_group_to_words(satang) + 'สตางค์') if satang > 0 else 'ถ้วน'
    return text


# ─── PDF Generation ────────────────────────────────────────────────────────────

def generate_pdf(config: dict, slip_png: str, font_dir: Path) -> bytes:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    from reportlab.pdfgen import canvas
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from PIL import Image

    pdfmetrics.registerFont(TTFont('Sarabun', str(font_dir / 'Sarabun-Regular.ttf')))
    pdfmetrics.registerFont(TTFont('SarabunBold', str(font_dir / 'Sarabun-Bold.ttf')))

    tmp = tempfile.NamedTemporaryFile(suffix='.pdf', delete=False)
    tmp.close()

    c = canvas.Canvas(tmp.name, pagesize=A4)
    W, H = A4
    margin = 2.0 * cm
    inner_w = W - 2 * margin

    y = H - margin

    # ── Title ──
    c.setFont('SarabunBold', 15)
    title = 'แบบฟอร์มใบแจ้งการชำระเงินค่าซื้อเอกสารประกวดราคาอิเล็กทรอนิกส์'
    c.drawCentredString(W / 2, y, title)
    y -= 0.5 * cm

    # ── Divider ──
    c.setLineWidth(1)
    c.line(margin, y, W - margin, y)
    y -= 0.6 * cm

    # ── Fields ──
    LABEL_W = 5.0 * cm
    FS = 13

    def draw_field(label: str, value: str):
        nonlocal y
        c.setFont('SarabunBold', FS)
        c.drawString(margin + 0.3 * cm, y, label)
        c.setFont('Sarabun', FS)
        c.drawString(margin + LABEL_W, y, value)
        # underline for value
        c.setLineWidth(0.5)
        c.line(margin + LABEL_W, y - 2, W - margin - 0.3 * cm, y - 2)
        y -= 0.85 * cm

    amount = config['amount']
    amount_str = f"{amount:,.2f} บาท  ({baht_to_words(amount)})"

    fields_top = y
    draw_field('เลขโครงการ e-GP :', config['project_id'])
    draw_field('หน่วยงาน :', config['agency_name'])
    draw_field('ธนาคาร :', config['bank'])
    draw_field('เลขบัญชี :', config['account_no'])
    draw_field('จำนวนเงิน :', amount_str)
    draw_field('ชื่อผู้ชำระเงิน :', config['payer_name'])
    draw_field('เบอร์โทรศัพท์ :', config['payer_phone'])

    fields_bottom = y
    # (border around fields removed per user rule -- no box on details section)
    y -= 0.4 * cm

    # ── Slip label ──
    c.setFont('SarabunBold', 13)
    c.drawString(margin, y, 'หลักฐานการชำระเงิน (สลิป) :')
    y -= 1.0 * cm

    # ── Slip image ──
    img = Image.open(slip_png)
    iw, ih = img.size

    max_w = inner_w
    max_h = H - (H - y) - margin - 0.5 * cm  # remaining space
    max_h = min(max_h, 12 * cm)

    scale = min(max_w / iw, max_h / ih)
    draw_w = iw * scale
    draw_h = ih * scale

    x_img = margin + (inner_w - draw_w) / 2
    c.drawImage(slip_png, x_img, y - draw_h, width=draw_w, height=draw_h,
                preserveAspectRatio=True)

    # Box around slip
    c.setLineWidth(1)
    c.rect(margin, y - draw_h - 0.2 * cm, inner_w, draw_h + 0.5 * cm, stroke=1, fill=0)

    c.save()

    with open(tmp.name, 'rb') as f:
        data = f.read()
    os.unlink(tmp.name)
    return data


# ─── Save with Thai filename (bytes workaround) ────────────────────────────────

# b'ใบแจ้งการ' in UTF-8 — used to locate the target subfolder
_SUBFOLDER_MARKER = b'\xe0\xb9\x83\xe0\xb8\x9a\xe0\xb9\x81\xe0\xb8\x88\xe0\xb9\x89\xe0\xb8\x87\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3'

def _find_log_dir() -> bytes:
    """
    ค้นหา log_dir อัตโนมัติ ลำดับ:
    0. /sessions/*/mnt/ — target folder (ใบแจ้งการ...) mount โดยตรง ← PRIORITY
    1. /sessions/*/mnt/[EGP]_E-BIDDING*/Log/
    2. /sessions/*/mnt/*/E-BIDDING/Log/
    3. /sessions/*/mnt/Downloads/ (fallback)
    """
    import glob
    # Pattern 0: target folder mounted directly under mnt/
    for mnt in glob.glob('/sessions/*/mnt/'):
        mnt_b = mnt.encode('utf-8').rstrip(b'/')
        try:
            for entry in os.scandir(mnt_b):
                if _SUBFOLDER_MARKER in entry.name:
                    print('  ✅ Target folder mounted directly — saving there')
                    return mnt_b  # save_pdf scandir will find the subfolder
        except OSError:
            pass
    # Pattern 1: [EGP]_E-BIDDING* (main DB folder)
    for p in glob.glob('/sessions/*/mnt/[[]EGP[]]*E-BIDDING*/Log/'):
        return p.encode('utf-8').rstrip(b'/')
    # Pattern 2: any mounted */E-BIDDING/Log/
    for p in glob.glob('/sessions/*/mnt/*/E-BIDDING/Log/'):
        return p.encode('utf-8').rstrip(b'/')
    # Fallback: Downloads
    for p in glob.glob('/sessions/*/mnt/Downloads/'):
        print('  ⚠️  E-BIDDING folder not mounted — saving in Downloads')
        return p.encode('utf-8').rstrip(b'/')
    raise RuntimeError('No suitable save directory found')


def save_pdf(data: bytes, config: dict) -> str:
    agency_short = config['agency_short']
    project_id = config['project_id']
    fname = f"ใบแจ้งชำระเงินค่าซื้อเอกสาร_{agency_short}_{project_id}.pdf"

    # Use config log_dir if provided and exists, else auto-detect
    cfg_log = config.get('log_dir', '')
    log_dir_bytes = cfg_log.encode('utf-8').rstrip(b'/') if cfg_log else b''
    if log_dir_bytes and not os.path.isdir(log_dir_bytes):
        log_dir_bytes = b''
    if not log_dir_bytes:
        log_dir_bytes = _find_log_dir()

    # Find Thai subfolder using bytes scandir (OneDrive encoding workaround)
    target_dir = None
    try:
        for entry in os.scandir(log_dir_bytes):
            if _SUBFOLDER_MARKER in entry.name:
                target_dir = entry.path
                break
    except (OSError, NotADirectoryError):
        pass

    if target_dir is None:
        # Fallback: save directly in log_dir
        print('  ⚠️  Target subfolder not found — saving in log_dir directly')
        target_dir = log_dir_bytes

    dest = target_dir + b'/' + fname.encode('utf-8')
    with open(dest, 'wb') as f:
        f.write(data)

    return fname


# ─── Main ──────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print('Usage: python generate_fee_pdf.py <config.json>')
        sys.exit(1)

    cfg_path = sys.argv[1]
    with open(cfg_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    print('Checking dependencies...')
    try:
        import reportlab, PIL  # noqa
    except ImportError:
        install_deps()

    print('Preparing fonts...')
    font_dir = ensure_fonts()

    print('Converting slip...')
    slip_png = slip_to_png(config['slip_path'])

    print('Generating PDF...')
    pdf_data = generate_pdf(config, slip_png, font_dir)

    print('Saving PDF...')
    fname = save_pdf(pdf_data, config)

    print(f'Done: {fname}')


if __name__ == '__main__':
    main()
