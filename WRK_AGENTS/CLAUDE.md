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
- 👑 Preview สิทธิ์นายเท่านั้น — แสดง visual preview ทุกครั้งที่แก้ไข UI (ห้าม skip)

## 📁 Files & URLs
- Main: `rmn_ebidding_tracker_2.html` (single source of truth)
- Logo: `assets/logo.png`
- Proxy: `netlify/functions/proxy.js`
- Live: https://m4dm4rx.github.io/RMN-eBidding-Workflow/
- Repo: https://github.com/m4dm4rx/RMN-eBidding-Workflow.git

## 🏗️ Backbone
M4RX-B4SE/RMN_Enterprise/E-Bidding/

## 🖥️ Multi-Machine
- CMD: ใช้ `%USERPROFILE%` เสมอ — ห้าม hardcode path
- Mounts: `RMN-eBidding-Workflow` / `E-BIDDING` / `Downloads`

## 🔀 Git Push (ส่งทีละบรรทัด — ห้ามรวม)
```
git -C "%USERPROFILE%\OneDrive\Claude\Projects\RMN-eBidding-Workflow" add <file>
git -C "%USERPROFILE%\OneDrive\Claude\Projects\RMN-eBidding-Workflow" commit -m "msg"
git -C "%USERPROFILE%\OneDrive\Claude\Projects\RMN-eBidding-Workflow" push
```
> GitHub Pages deploy จาก branch `main` (ไม่ใช่ master)
> push ธรรมดาได้เลย ไม่ต้อง push origin main:master อีกต่อไป

## 🎨 UI Rules
- Light mode default · Viewer URL: `?view=1` (mobile) · Editor: no param (desktop)
- View mode: ซ่อน data-edit-only, theme btn, ปรับ tab labels สั้น
- KPI border-left accent · filter inputs pill-shape · expand btn = text-link

## 📋 STATUS values
รอผลพิจารณา/เป็นผู้เสนอต่ำสุด · ไม่ได้เป็นผู้เสนอต่ำสุด · อนุมัติสั่งจ้าง · จัดทำสัญญา · แพ้การประมูล · แพ้/ขาดคุณสมบัติ · ยกเลิกโครงการ · ห้างขอยกเลิก

## 🤖 Agents
แต่ละ agent มีหน้าที่เดียวเท่านั้น — ห้ามรับงานนอกขอบเขต
| Agent | แก้ได้ | ห้ามแตะ |
|---|---|---|
| MAPMAKER | PDF แผนที่ | อื่นทั้งหมด |
| E-BIDDING DOC FEE | `doc_fees.json` เท่านั้น | tracker HTML |
| BIDDING OPERATING | `seed_bids.js` เท่านั้น | tracker HTML, doc_fees.json |
| UI/UX EDITOR | tracker HTML (UI/CSS/layout/logic) | `DOC_FEES` array, fetch URL |

## 🔒 Data Separation Rules (CRITICAL)
- **Source of truth คือ `doc_fees.json` เท่านั้น** — ห้าม hardcode data ลงใน tracker HTML
- `const DOC_FEES = [];` ใน tracker HTML ต้องเป็น array เปล่าเสมอ — ห้าม agent ใดเขียนข้อมูลลงไป
- `fetch('https://raw.githubusercontent.com/m4dm4rx/RMN-eBidding-Workflow/main/doc_fees.json')` — ห้าม uiux-editor เปลี่ยน URL นี้
- ถ้า uiux-editor แก้ HTML แล้วเห็น DOC_FEES มีข้อมูล → ลบทิ้ง ใส่ `[]` แทนทันที

## 🔄 Session State (2026-06-16)
### ✅ Done (UI/UX Agent — session นี้)
- Restore saveBid/editBid/deleteBid ที่หายไปตอน API cleanup ✅
- Dashboard แสดงทุกปีงบ (Store.getAll) ✅
- ซ่อน year-tabs บน Dashboard tab ✅
- ลบ label "ปีงบประมาณ 2569" ออกจาก header/subtitle ✅
- Growth chart (dual-axis bar) layout 2×2 + Chart.js CDN ✅
- SME rewrite → จำนวนโครงการต่อห้าง แทน 300M tracker ✅
- ลบ card % ลดราคาเฉลี่ย (NaN bug) ✅
- Province chart ซ่อน ? (records ไม่มี province) ✅
- Normalize entity names ใน seed_bids.js ✅
  - "ห้างหุ้นส่วน" → "ห้างหุ้นส่วน RMN" (208 records)
  - "กิจการร่วมค้า" + "ร่วมค้า RMN" → "กิจการร่วมค้า RMN" (23)
  - "ร่วมค้า รักดี" → "กิจการร่วมค้า รักดี" (7)

### 📦 Entity Structure (confirmed)
| Entity | บทบาท | Records |
|---|---|---|
| ห้างหุ้นส่วน RMN | ห้างหลัก | 322 |
| กิจการร่วมค้า RMN | ร่วมค้ากับ รุ่งเรืองชัยฯ (เลิกใช้) | 23 |
| กิจการร่วมค้า รักดี | ร่วมค้ากับ รักดี การโยธา | 7 |
| กิจการร่วมค้า ตักสิลา | ร่วมค้ากับ ตักสิลา อาร์เอ็มเอ็น | 4 |

### ⚠️ รู้จัก — ยังไม่ลง
- กิจการร่วมค้า ตักสิลา มี 11 records ปี 2568 จากระบบเก่า (ยังไม่มีราคา)
- HEAD.lock / index.lock ค้างบ่อย → user ต้อง del ก่อน push ทุกครั้ง

### ⏳ Pending (Tracker)
- รอผล seq 99-100 → อัปเดต status + midPrice
- light mode toggle (dev agent)
- FIX 7 phase 2: one-off structural styles (dev agent)

### ⏳ Pending (Map Maker)
- ทต_แวงน่าง / อบต_ยางใหญ่ → ทำใหม่ session ใหม่
- ทม_สกลนคร (52.3 กม.) → ทำใหม่ session ใหม่
- อบต_ทรายมูล (62.9 กม.) → ทำใหม่ session ใหม่

## 🔄 Session State (2026-06-25)
### ✅ Done (session นี้)
- Modal popup: click project ID → popup รายละเอียด (pipeCard + projectCard) ✅
- Fix JS syntax error (backtick escape จาก Python heredoc) ✅
- Fix paid flag bug (reg truthy → ขึ้น จ่ายแล้ว ผิด) ✅
- pipeCard header redesign: ID+Agency+Status badge row + "ดูรายละเอียด ▶" ✅
- B+D contrast: badge row bg + project name left accent bar ✅
- Tab ค่าเอกสาร (renderDocFeeTab): ตาราง + paid/email toggle ✅
- Dashboard section ค่าเอกสาร (renderDashDocFee): รอจ่าย/รอส่ง email เท่านั้น ✅
- ลบ SME tab → ย้ายเป็น card ใน Dashboard ✅
- Viewer dark/light toggle switch (#view-theme-toggle) ✅
- Dashboard docfee: ลบ เรียบร้อย section, แสดงเฉพาะ pending ✅
- paid badge: clickable → toggleDocFeePaid() (true/false/null cycle) ✅
- Tab ค่าเอกสาร: col ช่วงเวลาการชำระเงิน, swap วิธีจ่าย→emailTo ✅
- fmtThaiDate(): "2569-06-25" → "25/มิ.ย./2569" ✅
- Tab ค่าเอกสาร: ลบ ฿, ซ่อน year-tabs, sort ใหม่สุดบน ✅
- SME card: วงเงินสะสม vs 300M limit (🟢<80% 🟡≥80% 🔴≥100%) ✅
- ลบ KPI card "ค่าเอกสารประมูลรวม" (ซ้ำกับ section renderDashDocFee) ✅

### 📋 doc_fees.json schema ใหม่ (Doc Fee Agent ต้องเพิ่ม)
| field | ความหมาย |
|---|---|
| feeStartDate | วันเริ่มจ่ายค่าเอกสาร (YYYY-MM-DD) |
| feeEndDate | วันสิ้นสุดจ่ายค่าเอกสาร (YYYY-MM-DD) |
| emailTo | email หน่วยงานที่ส่งหลักฐาน |

### ⏳ Pending
- topbar + tabs: เปลี่ยน bg จาก backdrop-filter blur → solid (ให้เหมือน section row 3)
- light mode toggle full implementation (dev agent)
- FIX 7 phase 2: one-off structural styles (dev agent)
- Map Maker: ทต_แวงน่าง / อบต_ยางใหญ่ / ทม_สกลนคร / อบต_ทรายมูล

## 🔄 Session State (2026-06-25 — E-Bidding Operating Agent)
### ✅ Done (session นี้)
- seq 127 อบต.เมืองเสือ มค. bid 796,000 ✅ ต่ำสุด
- seq 128 ทต.ปาฝา รอ. bid 598,000 ✅ ต่ำสุด
- seq 129 ทต.ศรีโคตร รอ. bid 568,000 ✅ ต่ำสุด
- seq 130 อบต.ม่วงลาย สน. bid 1,078,000 ✅ ต่ำสุด
- seq 131 อบต.หนองบัว หบ. bid 758,000 ✅ ต่ำสุด
- seq 132 อบต.โนนข่า ขก. bid 4,898,000 ❌ ไม่ต่ำสุด (-53,000) lowest 4,845,000
- seq 133 รพ.สุวรรณคูหา หบ. bid 1,558,000 ✅ ต่ำสุด
- seq 134 ทต.โคกพระ มค. bid 378,000 ✅ ต่ำสุด
- seq 135 ทต.ธัญญา กส. bid 598,000 ✅ ต่ำสุด
- seq 136 อบต.ปางกู่ หบ. bid 1,748,000 ✅ ต่ำสุด
- Lock format: SEQ summary line + 5-col table (เลขที่/หน่วยงาน/ที่ตั้งหน่วยงาน/ราคายื่น/Plant)

### 📋 Rules confirmed this session
- plantDist = เลขในวงเล็บ (เช่น "(สารคาม55)") — ไม่ใช่คอลัมน์ขวาสุด
- ชื่อหน่วยงาน: ถ้า PDF ≠ ตาราง → ใช้ PDF เสมอ (เช่น โนนข่า ≠ โนนซ่า, ปาฝา ≠ ปาฬา)
- ม่วงลาย วันยื่น 24 มิ.ย. (ตารางผิด บอก 22)

### ⏳ Pending
- (none)
push doc_fees.json (user ต้องรันเอง)

## 🖥️ Multi-Machine
+ - ใช้ PowerShell เป็นหลักเสมอ — ห้ามใช้ CMD
- CMD: ใช้ `%USERPROFILE%` เสมอ — ห้าม hardcode path
+ - PowerShell: ใช้ `$env:USERPROFILE` เสมอ — ห้าม hardcode path