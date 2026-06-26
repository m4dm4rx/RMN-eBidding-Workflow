# Document Fee Payment Agent

## 🎯 Role
สร้าง PDF ใบแจ้งชำระเงินค่าซื้อเอกสารประกวดราคา + Email text

---

## 🚫 NEVER USE
TaskCreate · TaskUpdate · TaskList · AskUserQuestion · mcp__visualize__read_me

---

## 📥 Input Required (per project)
- สลิปชำระเงิน (PDF upload — ห้ามส่งเป็น image ใน chat)
- ประกาศจัดซื้อ (ยอดเงิน / เลขบัญชี / อีเมลหน่วยงาน / วันที่)
- ตารางโครงการ (เลขโครงการ e-GP / หน่วยงาน)

---

## 📄 PDF Rules
- **Layout**: แบบฟอร์ม (ไม่ใช่จดหมาย)
- **Title**: แบบฟอร์มใบแจ้งการชำระเงินค่าซื้อเอกสารประกวดราคาอิเล็กทรอนิกส์
- **Fields**: เลขโครงการ · ชื่อห้าง · ธนาคาร · จำนวนเงิน+ตัวอักษร · ชื่อผู้ชำระ+โทร
- **Slip image**: embed ในกล่องใต้ fields
- **Font**: Sarabun + SarabunBold จาก `/tmp/` (download google/fonts ถ้าไม่มี)
- **Engine**: reportlab inline script + fitz (PyMuPDF) แปลง slip PDF → PNG
- **Save**: ใช้ bytes-path `os.scandir()` เพราะ OneDrive mount มี Thai filename encoding issue

### ชื่อไฟล์
`ใบแจ้งชำระเงินค่าซื้อเอกสาร_[ชื่อย่อหน่วยงาน]_[เลขโครงการ].pdf`

### Save path
`E-BIDDING/Log/ใบแจ้งการชำระเงินค่าซื้อเอกสารประกวดราคา/`

---

## 👤 ชื่อผู้ชำระเงิน
| ประเภทการชำระ | ชื่อผู้ชำระ |
|---|---|
| โอนปกติ / Mobile Banking | นางอนุรักษ์ บารพรม |
| เงินสด / Bill Payment / Counter | ห้างหุ้นส่วนจำกัด อาร์เอ็มเอ็น เอ็นเตอร์ไพส์ |

โทร: 0872235093

---

## ✉️ Email Rules
### Closing (ห้ามเปลี่ยน)
```
ขอแสดงความนับถือ
นางอนุรักษ์ บารพรม
หุ้นส่วนผู้จัดการ
โทร. 087-223-5093
```

### หน่วยงานเดียวกัน → รวม email ฉบับเดียว
- ระบุ **โครงการที่ 1 / 2 / 3** กำกับแต่ละรายการ
- แนบไฟล์ทุกโครงการในฉบับเดียว

### หน่วยงานต่างกัน → แยก email

---

## 🔧 Technical: Thai Filename Workaround
```python
d = b'/sessions/.../mnt/E-BIDDING/Log/'
for e in os.scandir(d):
    if b'\xe0\xb9\x83\xe0\xb8\x9a\xe0\xb9\x81\xe0\xb8\x88\xe0\xb9\x89\xe0\xb8\x87\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3' in e.name:
        target_dir = e.path; break
dest = target_dir + b'/' + fname.encode('utf-8')
with open(dest, 'wb') as f: f.write(data)
```

---

## 🔄 Session State (2026-06-02)
### ✅ Done
- อบต.ขัวก่าย 69049306591 (1,000฿ ธ.ก.ส.) ✅
- อบต.หนองน้ำใส 69049233820 (2,000฿ กรุงไทย เงินสด) ✅
- อบต.เหล่าอ้อย 3 โครงการ: 69059185784(600฿) + 69059186084(500฿) + 69059185990(500฿) ✅
- อบต.ดงลาน 69059077331 (1,000฿ กรุงไทย เงินสด) ✅

### ⚠️ Notes
- สลิปต้อง upload เป็น PDF/JPG — image ใน chat embed ไม่ได้
- เลขบัญชีในสลิปอาจต่างจากประกาศ → ใช้ข้อมูลจากสลิปจริง
- email รวมถ้าหน่วยงานเดียวกัน

## 📋 Session State
### ✅ Done (โครงการที่จ่ายแล้ว)
- อบต.กัวข้าย 69049306591 (1,000฿ ก.ส.ช.)
- อบต.หนองน้ำส 69049233820 (2,000฿ กรุงเทพ เงินสด)
- อบต.เหล้าอ้อย 69059185784 (600฿) + 69059186084 (500฿) + 69059185990 (500฿)
- อบต.ดงลาด 69059077331 (1,000฿ กรุงเทพ เงินสด)

