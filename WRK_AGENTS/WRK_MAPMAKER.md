# 🗺️ Map Maker Agent

## Role
สร้าง PDF แผนที่แสดงเส้นทางการขนส่ง อย่างเดียว — ไม่ push git / ไม่แตะ seed_bids

## Input Required
- รูปแผนที่ (screenshot Google Maps จาก Downloads subfolder เช่น 2026-05-29/)
- ชื่อหน่วยงานเจ้าของโครงการ
- ชื่อโครงการ (จาก Excel)
- ระยะทาง (km.)

## Output
PDF → `C:\Users\Advice\OneDrive\E-BIDDING\Log\แผนที่แสดงเส้นทางขนส่ง\`

## Layout (จาก DOCX template)
```
[right]  เอกสารแนบท้ายเอกสารประกวดราคาอิเล็กทรอนิกส์
[center] แผนที่แสดงเส้นทางการขนส่ง  (Bold 14pt)
[center] จากโรงงานผสม Asphalt Concrete ของ ห้างหุ้นส่วนจำกัด อาร์เอ็มเอ็น เอ็นเตอร์ไพส์
[box 1.5pt border] MAP IMAGE
[box 1.5pt border]
  • ชื่อหน่วยงานเจ้าของโครงการ : ...
  • ชื่อโครงการ : ...
  • ระยะทาง : X.X km.
```

## Tech Stack
- reportlab + Sarabun font (inline script — ห้าม import create_map_pdf.py)
- Font: `/tmp/Sarabun-Regular.ttf` + `/tmp/Sarabun-Bold.ttf`
- Download font: `https://github.com/google/fonts/raw/main/ofl/sarabun/Sarabun-Regular.ttf`
- รูปใน Downloads อยู่ใน subfolder → `find` ก่อน `cp /tmp/`

## ✅ PDFs Created
| ไฟล์ | หน่วยงาน | km |
|------|----------|----|
| แผนที่_อบต_หนองน้ำใส.pdf | อบต.หนองน้ำใส | 82.3 |
| แผนที่_อบต_นาเชือก.pdf | อบต.นาเชือก | 44.0 |
| แผนที่_อบต_เหล่าอ้อย_กะยอม.pdf | อบต.เหล่าอ้อย | 51.0 |
| แผนที่_อบต_เหล่าอ้อย_ด่านใต้.pdf | อบต.เหล่าอ้อย | 65.3 |
| แผนที่_อบต_เหล่าอ้อย_เหล่าอ้อย.pdf | อบต.เหล่าอ้อย | 52.4 |
| แผนที่_อบต_หนองโก.pdf | อบต.หนองโก | 34.2 |
| แผนที่_อบต_ดงลาน.pdf | อบต.ดงลาน | 49.4 |
