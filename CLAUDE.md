# RMN e-Bidding Tracker

## ⚙️ Workflow Reminder (Claude behavior rules)
- **ประหยัด Tokens**: ไม่สร้าง TaskList / ไม่ถาม AskUserQuestion / ไม่โหลด ToolSearch สำหรับงานที่ไม่จำเป็น
- **ตอบสั้น ตรงประเด็น** — ไม่ขยายความโดยไม่จำเป็น
- **คิดทีละ Step** — วิเคราะห์ก่อน ลงมือทีละขั้น ไม่ข้ามขั้นตอน
- **ห้ามเดาข้อมูล** — ถ้าไม่มีข้อมูลชัดเจน ให้ถามก่อน ไม่สมมติค่า

## 🎨 UI/Coding Role Rules
- **Role**: UI/Coding Master
- **Output**: Compact Diff/Change-log only — **NEVER preview full code or full tables**
- **State**: Maintain workflow state across short inputs
- **Format**: 50/50 Human-readable + clean code
- **Style**: Reply directly — no intro/outro chatter
- **Anchor Rules** *(strict, always enforced)*:
  1. Do NOT output full file / full code block / full table — Diff/Change-log only
  2. Think step-by-step before acting — analyze → plan → execute
  3. Never hallucinate data, values, or field names — if unclear, ask first

Web app ติดตามการประมูลโครงการถนน ปีงบประมาณ 2569.

## Files
- `rmn_ebidding_tracker_2.html` — single source of truth (HTML + SEED_BIDS data)
- `netlify/functions/proxy.js` — CORS proxy for opend.data.go.th API
- Live: https://dorpnightmare-wq.github.io/rmn-ebidding-tracker/rmn_ebidding_tracker_2.html
- GitHub: https://github.com/dorpnightmare-wq/rmn-ebidding-tracker.git
- Deployments: https://github.com/dorpnightmare-wq/rmn-ebidding-tracker/deployments

## เวลาผลเบื้องต้นประมูล e-GP
- รอบเช้า → ผลออก **12:01 น.**
- รอบบ่าย → ผลออก **16:01 น.**

## Data entry workflow
1. User pastes row(s) from Excel → Claude **แปลงเป็น text** แสดงข้อมูลที่ parse ได้ (id, name, agency, province, budget, bid, date, status)
2. User ยืนยัน → Claude add to SEED_BIDS in HTML
3. User ยืนยัน push → git push → GitHub Pages auto-deploys

**Excel columns (left→right):**
1. เลขที่โครงการ (id เช่น 69049395087)
2. ชื่อโครงการ (name — long text)
3. หน่วยงาน (agency)
4. จังหวัด (province)
5. งบประมาณ (budget)
6. หมายเหตุ — contains bid after "ยื่น" keyword (เช่น "ยื่น 1,318,000")
7. วันที่/เวลา (date — เช่น "11 พ.ค.69 เวลา 9.00น." → "2569-05-11")
8. (ignore)

**Default values when adding:**
- `entity`: "ห้างหุ้นส่วน RMN"
- `status`: ดูจากผลเบื้องต้นวันประมูล
  - ราคาเราต่ำสุด (ชนะเบื้องต้น) → `"รอผลพิจารณา / เป็นผู้เสนอราคาต่ำสุด"`
  - ราคาเราไม่ต่ำสุด (แพ้เบื้องต้น) → `"รอผลพิจารณา / ไม่ได้เป็นผู้เสนอราคาต่ำสุด"`
- `seq`: next number after last entry
- `pct`: `Math.round((budget - bid) / budget * 10000) / 100` (0 if no budget)

## Git push commands
**กฎสำคัญ**: sandbox push GitHub ไม่ได้ (ไม่มี credentials) — ต้องให้ user รันจาก CMD เสมอ
**ส่งทีละบรรทัด** ห้ามรวมกัน เพราะ copy-paste แล้วจะติดกันเป็น error "git: 'pushgit' is not a git command"

```
del "C:\Users\Advice\OneDrive\Claude\Projects\RMN e-Bidding Tracker\.git\HEAD.lock"
```
```
git -C "C:\Users\Advice\OneDrive\Claude\Projects\RMN e-Bidding Tracker" add rmn_ebidding_tracker_2.html
```
```
git -C "C:\Users\Advice\OneDrive\Claude\Projects\RMN e-Bidding Tracker" commit -m "Add seq XX: agency date"
```
```
git -C "C:\Users\Advice\OneDrive\Claude\Projects\RMN e-Bidding Tracker" push
```

## STATUS values (stored in data)
- รอผลพิจารณา / เป็นผู้เสนอราคาต่ำสุด
- รอผลพิจารณา / ไม่ได้เป็นผู้เสนอราคาต่ำสุด
- อนุมัติสั่งจ้าง/ประกาศให้เป็นผู้ชนะ
- จัดทำสัญญาแล้ว
- แพ้การประมูล
- แพ้เนื่องจากขาดคุณสมบัติ/เอกสารไม่สมบูรณ์
- ยกเลิกโครงการ
- ห้างขอยกเลิกเอง

## UI / Layout สำคัญ
- **View mode tabs**: แสดงแค่ 3 tabs → Dashboard, รายงานข้อมูลโครงการ, รายงานแบ่งตามยอด SME (Records tab ซ่อนด้วย `data-edit-only`)
- **Project cards พับได้**: ค่าเริ่มต้น collapsed แสดง status badge + เลขโครงการ + หน่วยงาน + วันที่ + ยอดยื่น + ปุ่ม "รายละเอียด ▽" กดเพื่อขยาย/ซ่อน
- **Recent Wins Timeline**: อยู่ใน Dashboard เท่านั้น (ลบออกจาก Report tab แล้ว)
- **Report tab**: มี filter bar — search + status + entity + agency + sort
- **Badge status**: ใช้ชื่อเต็มทุกที่ ไม่ตัดย่อ
- **Dashboard KPI**: มี Competitor Leaderboard (บาร์แสดงคู่แข่งที่ได้งานไปแทน นับจำนวนครั้ง)

## แผนที่ PDF workflow (เอกสารแนบ e-GP)
1. User ส่ง screenshot Google Maps (route จาก RMN Enterprise Asphalt → โครงการ) เป็น **ไฟล์ upload**
2. Claude สร้าง `แผนที่_[id].pdf` ด้วย **reportlab + Sarabun font** โดยตรง
   - **บันทึกที่**: `C:\Users\Advice\OneDrive\E-BIDDING\Log\แผนที่แสดงเส้นทางขนส่ง\แผนที่จากที่ตั้งโรงงานถึงหน้างาน_[agency]_[id].pdf`
   - **ห้ามใช้ LibreOffice แปลง** — sandbox ไม่มี Thai font → ข้อความเป็นกล่องทั้งหมด
   - **ห้ามสร้าง docx แล้วแปลง** — ใช้ reportlab ตรงๆ เท่านั้น
3. โครงสร้างเอกสาร (A4, Sarabun font):
   - หัวขวา (underline, 14pt): "เอกสารแนบท้ายเอกสารประกวดราคาอิเล็กทรอนิกส์"
   - หัวกลาง (bold 26pt): "แผนที่แสดงเส้นทางการขนส่ง"
   - subheading ซ้าย (16pt, wrap): "จากโรงงานผสม Asphalt Concrete ของ ห.จ.ก. อาร์เอ็มเอ็น เอ็นเตอร์ไพส์"
   - กล่องรูปแผนที่ (border 2pt, image เต็มกล่อง)
   - กล่องข้อความ (border 2pt, bullet 16pt, label bold):
     - **ชื่อหน่วยงานเจ้าของโครงการ**: [agency]
     - **ชื่อโครงการ**: [name เต็ม — wrap หลายบรรทัด]
     - **ระยะทาง**: [XX] กม.
4. User อัพโหลด PDF ใน e-GP ได้เลย ไม่ต้องแปลงเพิ่ม

**Font setup** (ทำครั้งแรก หรือถ้า /tmp/Sarabun-Regular.ttf หาย):
```python
import urllib.request
BASE = "https://raw.githubusercontent.com/google/fonts/main/ofl/sarabun/"
urllib.request.urlretrieve(BASE + "Sarabun-Regular.ttf", "/tmp/Sarabun-Regular.ttf")
urllib.request.urlretrieve(BASE + "Sarabun-Bold.ttf", "/tmp/Sarabun-Bold.ttf")
```

**ชื่อไฟล์**: `แผนที่จากที่ตั้งโรงงานถึงหน้างาน_[agency]_[id].pdf`
**บันทึกที่**: `C:\Users\Advice\OneDrive\E-BIDDING\Log\แผนที่แสดงเส้นทางขนส่ง\`

**หมายเหตุ**: ห้าม import จาก create_map_pdf.py — มีปัญหา `__pycache__` ทำให้ code ใหม่ไม่ถูกโหลด
ให้เขียน script inline ใน bash แทนทุกครั้ง เช่น:
```python
filename = f"แผนที่จากที่ตั้งโรงงานถึงหน้างาน_{agency}_{project_id}.pdf"
out_path = f"/sessions/.../mnt/E-BIDDING/Log/แผนที่แสดงเส้นทางขนส่ง/{filename}"
```

**reportlab canvas approach** (ไม่ใช้ Platypus/Frame — ใช้ canvas วาดตรงๆ ควบคุม position ได้เต็มที่):
```python
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
pdfmetrics.registerFont(TTFont('Sarabun', '/tmp/Sarabun-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Sarabun-Bold', '/tmp/Sarabun-Bold.ttf'))
```

## Entity options
- ห้างหุ้นส่วน RMN (default)
- กิจการร่วมค้า RMN
- กิจการร่วมค้า ตักสิลา
