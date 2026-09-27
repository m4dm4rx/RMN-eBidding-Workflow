# WRK_OPERATING — Session State & Pending (OPY)

> กฎทั้งหมดอยู่ที่ `WRK_OPERATING.md` · ไฟล์นี้เก็บ **state ล่าสุด + pending** เท่านั้น
> เขียน state ทุกครั้งที่งานเสร็จเป็นก้อน **ห้ามรอตอนจบ session** · เพดาน 20 KB — เกินแล้วตัด state เก่าสุดออก (ประวัติอยู่ใน git log)

## 🔄 Session State (2569-09-27)
- **Last SEQ (FY2569) = 231** · `seed_bids.js` **648 records** (FY2569 = 231) · `doc_fee_queue.json` **27** pending **0** · `doc_fees.json` **37** · holes `[]`
- 🧭 **OPY = super agent** — รับ scope DOC (09-02) + MM (09-25) · UI ปิด 09-26 → งาน tracker/เว็บไป Linear `P-RMN-4` (Codex) · OPY **ไม่แก้ระบบ** งานแก้ระบบ → แจ้ง Marx เปิดใน Linear
- 📂 **repo ย้าย OneDrive → `C:\Repos\RMN-eBidding-Workflow`** (เจอตอน stage ล้มเหลว 09-25) · โฟลเดอร์ที่ grant ไว้ = ตัว repo ตรงๆ ไม่ใช่ `C:\Repos` ทั้งก้อน → เข้า `C:\Repos\M4RX-B4SE` (KB) ไม่ได้
- 📄 ปลายทาง PDF (แผนที่/ค่าเอกสาร/bid record) ชี้ไป **Drive Workflow Logs** แล้ว — commit `128d598` (RMN-18)
- 📏 `WRK_OPERATING.md` ตัดเหลือ **20,203 B** (`de24cf6`) — ย้าย verbatim ลง archive: ระเบียบ กวจ. ว.515 · DOC disabled · MM disabled → แทนด้วย section `🧭 OPY = super agent`
- ✅ **กฎ verify ใหม่ (บทเรียน 09-17)**: `node --check` ไม่พอ — `[a,,b]` ผ่าน syntax แต่เป็น sparse array ทำ `renderDash()` พัง · ต้อง eval `SEED_BIDS` เช็ก `length` · `holes=[]` · dup id · dup FY/seq · pct · ต้นเหตุคือ `},,` จาก commit `3f185d7` ของ OPY เอง เงียบ 6 commits (Sir UI จับได้ แก้ `ea25633`)

### ผลประมูลรอบนี้ (SEQ 226–231)
| SEQ | id | หน่วยงาน (จว.) | ยื่น | ต่ำสุด | ผล |
|---|---|---|---|---|---|
| 226 | 69089552052 | อบต.โนนราษี (มค.) | 2,486,000 | 2,486,000 | ✅ ต่ำสุด |
| 227 | 69099172841 | ทต.โพนทอง (กส.) | 398,000 | 375,990 | ❌ −22,010 |
| 228 | 69099060167 | อบต.หนองไผ่ (รอ.) | 576,000 | 564,000 | ❌ −12,000 |
| 229 | 69099061215 | อบต.หนองไผ่ (รอ.) | 696,000 | 694,000 | ❌ −2,000 (เฉียด) |
| 230 | 69099409096 | อบต.สวนหม่อน (ขก.) | 356,000 | 356,000 | ✅ ต่ำสุด |
| 231 | 69099336753 | ทต.หนองแปน (กส.) | 396,000 | 396,000 | ✅ ต่ำสุด |

ทั้ง 6 งาน **ไม่มีค่าเอกสาร** (`no_fee_required`) · entity = หจก.รักดี การโยธา · plant มหาสารคาม ทุกงาน

### บทเรียนรอบนี้
- 📌 **SEQ231 `plantDist` 80 → 28.8** (2569-09-27) — "ล็อคแพล้น80กม." คือเพดาน TOR ไม่ใช่ระยะ · แผนที่ `แผนที่_ทต_หนองแปน_69099336753.pdf` ใน Drive ถูกแล้ว (รักดี · 28.8 km) ไม่ต้องทำใหม่ · มีแค่ record นี้ที่โดน
- 📌 **เลขในตาราง user ซ้ำ/ผิดได้** — SEQ 231 ตาราง copy เลขซ้ำจากแถวก่อน (`69099126557` ซึ่งเป็นของ SEQ 225) · ยึดเลขจาก **ชื่อไฟล์ `annoudoc_*.pdf`** แล้วถามยืนยันก่อนลง
- 📌 **`doc_*.pdf` ไม่มีราคากลาง** — ราคากลางอยู่ใน `annoudoc_*.pdf` เท่านั้น · ถ้าได้แต่ doc_ ให้ลง record ไปก่อนพร้อม flag แล้ว backfill (ทำกับ SEQ 230 · `d022acb`)
- 📌 ราคากลาง **สูงกว่าวงเงินได้** — SEQ 227 (+17.8%) · SEQ 231 (+24.2%) · ตรวจจาก PDF แล้วถูกต้อง ไม่ใช่ error
- 📌 `mcp__visualize__show_widget` **พังช่วง 09-25/09-26** — client แสดง Request JSON ดิบแทน visual · fallback = ส่ง HTML file ผ่าน `SendUserFile` หรือ plain text block
- 📌 ปุ่มคัดลอกใน widget: `navigator.clipboard` ถูกบล็อกใน iframe → ใช้ `<input readonly>` + `execCommand('copy')` + fallback select ให้ผู้ใช้กด Ctrl+C

## ⏳ Pending
- **ไม่มี pending งานประมูล** — ผลครบทั้ง 231 · queue pending 0
- 🔶 **Working folder / scope ใน `WRK_OPERATING.md` ยังไม่อัป** — Marx กำลังคุยกับ DA อยู่ (27 ก.ย.) **ห้ามแก้เองจนกว่า DA จะสรุป** · ประเด็น: grant เฉพาะ repo ไม่ใช่ `C:\Repos` · `rmn_ebidding_tracker_2.html` ยังอยู่ใน "ห้ามแตะ" ทั้งที่ UI ปิดแล้ว
- 🔶 `pct` 16 records เก่า (FY2569 seq 4,6,30,32,35,40,52,54,59,61,66,67,91,105,115,155) คำนวณจาก `midPrice` ไม่ใช่ `budget` — รอคำสั่งว่าจะ recompute ไหม
- 🔶 dup `FY/seq` 26 คู่ใน FY2566 (22) + FY2567 (4) — legacy ไม่กระทบ FY2569
- 🔶 format `doc_fee_queue.json` — OPY เปลี่ยนเป็น 1 บรรทัด/entry เองเมื่อ 09-16 (เดิม pretty-print) ยังไม่ได้ยืนยันจาก Marx
- 🔶 skill `fee-payment` ยังชี้ path PDF เก่า — **OPY แก้ `*.skill` เองไม่ได้**
- 🔶 commit `5d8ba58` (WRK_AGENTS/CLAUDE.md · coordinator) ค้างไม่ push — ไม่ใช่ไฟล์ของ OPY ไม่แตะ

> 📜 state 2569-09-03 (SEQ 220 · 637 records · doc_fees 36 · HEAD `74a24ec` · DB ปิดตัว) → `git log` + `WRK_OPERATING_ARCHIVE_2569H2.md`
> ⚠️ บทเรียนที่ยังใช้: SEQ217 วงเงินในตาราง user พิมพ์ผิด 50,000 จริง 500,000 — **ตัวเลขไม่สมเหตุผล = ถาม ห้ามเดา**
