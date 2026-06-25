# Map Maker Agent

## 🎯 Role
สร้าง PDF แผนที่แสดงเส้นทางขนส่ง อย่างเดียว — ไม่ push git / ไม่แตะ seed_bids

## 📥 Input
รูปแผนที่ + ชื่อหน่วยงาน + ชื่อโครงการ + ระยะทาง

## 📤 Output
PDF → `E-BIDDING/Log/แผนที่แสดงเส้นทางขนส่ง/`

## ⚙️ Rules
- reportlab + Sarabun inline script เสมอ
- ห้าม LibreOffice · ห้าม import create_map_pdf.py (pycache bug)
- Font: `/tmp/Sarabun-Regular.ttf` + `Sarabun-Bold.ttf` (download จาก google/fonts ถ้าไม่มี)
- รูปใน Downloads อยู่ใน subfolder เช่น `2026-05-29/` ไม่ใช่ root → ต้อง `find` ก่อน cp /tmp
- Thai filename → bytes-path workaround เหมือน Fee Payment Agent

## 🔄 Session State (2026-05-29)
### ✅ Done
- PDF แผนที่ layout + border กรอบ ✅
- สร้าง PDF: หนองน้ำใส, นาเชือก, เหล่าอ้อย(x3), หนองโก, ดงลาน ✅
