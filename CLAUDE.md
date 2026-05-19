# RMN e-Bidding Tracker

## 🚫 NEVER USE (no exceptions)
TaskCreate · TaskUpdate · TaskList · TaskStop · TaskGet · AskUserQuestion · mcp__visualize__read_me
ToolSearch → โหลดเฉพาะเมื่อ tool ไม่มีใน schema จริงๆ

## ⚙️ Core Rules
- Diff/changelog only — ห้าม output full file/table
- grep/bash หา section ก่อน — ห้าม Read ทั้งไฟล์
- Edit (diff) เสมอ — Write เฉพาะ full rewrite
- อ่านไฟล์ครั้งเดียว/task — ไม่อ่านซ้ำ verify
- ห้ามเดาข้อมูล — ถามก่อนถ้าไม่ชัด
- bash output → pipe | head -40 เสมอ — ห้าม dump .git/objects
- Auto-update MD @ 90% context → append ## 🔄 Session State → แจ้ง user เริ่ม session ใหม่
- คำนวณ usage ก่อนทุก Edit — ถ้า context ไม่พอ ห้าม Edit แจ้ง user แทน

## 📁 Files & URLs
- Main: `rmn_ebidding_tracker_2.html` (single source of truth)
- Logo: `assets/logo.png`
- Proxy: `netlify/functions/proxy.js`
- Live: https://dorpnightmare-wq.github.io/rmn-ebidding-tracker/rmn_ebidding_tracker_2.html
- Repo: https://github.com/dorpnightmare-wq/rmn-ebidding-tracker.git

## 🖥️ Multi-Machine
- CMD: ใช้ `%USERPROFILE%` เสมอ — ห้าม hardcode path
- Mounts: `RMN e-Bidding Tracker` / `E-BIDDING` / `Downloads`

## 📊 Data Entry (Excel → SEED_BIDS)
Cols: id | name | agency | province | budget | หมายเหตุ(bid หลัง"ยื่น") | date | (ignore)
Defaults: entity="ห้างหุ้นส่วน RMN" · seq=next · pct=round((budget-bid)/budget*10000)/100
Status: ต่ำสุด→"รอผลพิจารณา / เป็นผู้เสนอราคาต่ำสุด" · ไม่ต่ำสุด→"รอผลพิจารณา / ไม่ได้เป็นผู้เสนอราคาต่ำสุด"
ผลเช้า→12:01 · ผลบ่าย→16:01

## 🔀 Git Push (ส่งทีละบรรทัด — ห้ามรวม)
```
git -C "%USERPROFILE%\OneDrive\Claude\Projects\RMN e-Bidding Tracker" add rmn_ebidding_tracker_2.html
git -C "%USERPROFILE%\OneDrive\Claude\Projects\RMN e-Bidding Tracker" commit -m "msg"
git -C "%USERPROFILE%\OneDrive\Claude\Projects\RMN e-Bidding Tracker" push
```

## 🎨 UI Rules
- Light mode default · Viewer URL: `?view=1` (mobile) · Editor: no param (desktop)
- View mode: ซ่อน data-edit-only, theme btn, ปรับ tab labels สั้น
- KPI border-left accent · filter inputs pill-shape · expand btn = text-link

## 📋 STATUS values
รอผลพิจารณา/เป็นผู้เสนอต่ำสุด · ไม่ได้เป็นผู้เสนอต่ำสุด · อนุมัติสั่งจ้าง · จัดทำสัญญา · แพ้การประมูล · แพ้/ขาดคุณสมบัติ · ยกเลิกโครงการ · ห้างขอยกเลิก

## 🗺️ PDF Map
reportlab + Sarabun inline script · บันทึก: E-BIDDING/Log/แผนที่แสดงเส้นทางขนส่ง/
ห้าม LibreOffice · ห้าม import create_map_pdf.py (pycache bug) · เขียน script inline เสมอ
Font: /tmp/Sarabun-Regular.ttf + Sarabun-Bold.ttf (download จาก google/fonts)

## 🔄 Session State (2026-05-19)
### ✅ Done this session
- Perf analysis: ตรวจ 7 token drain risks พร้อม impact analysis
- FIX 2: debounce oninput renderReport/renderTable (200ms)
- FIX 4: rAF guard dedup renderDash ใน quickstatus handler
- FIX 5: debounce persist() 500ms + beforeunload flush (_persistNow)
- FIX 1: แยก SEED_BIDS → seed_bids.js (1,618 lines) + HTML ลดจาก 4,135 → 2,554 lines (-38%)
- Boot truncation restored: records-list click listener + change listener + copyViewLink + </script></body></html>
- FIX 3: renderBidTimeline pagination (PAGE_SIZE=20) + load-more button + App.timelineLoadMore()

### ⏳ Pending
- **Push ✅ done**
- FIX 6: CSS class refactor (inline styles → classes) — ทำทีหลัง/phase
- ตรวจสอบ light mode + timeline load-more หลัง push
