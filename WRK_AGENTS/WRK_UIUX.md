# 🎨 UI/UX Customize Agent
> เรียกสั้นว่า "UI" (แจ้งจาก DP 2569-07-27)

## 🎯 Role
Senior UI/UX Designer — ปรับ UI/UX ของ `rmn_ebidding_tracker_2.html` เท่านั้น
ไม่ยุ่งกับ data/logic/API/seed_bids

## 📋 My Tasks (this session)
> 📦 session log ก่อน 2026-09-08 ย้ายไป `WRK_AGENTS/WRK_UIUX_ARCHIVE_2569H2.md` แล้ว — ไม่ต้องอ่านตอนเปิด session

### ⏳ Pending UI tasks
- _(ว่าง)_ — `:root` dedup ปิดแล้ว 2026-09-08 ตามคำตัดสิน DA ทางเลือก A

### 🗒️ Context carried over (not a UI task, FYI for continuity)
- Mark กำลังคิดสถาปัตยกรรมใหญ่: แยกเป็น 2 BASE — "E-BIDDING BASE" (ของเดิม, public) vs "RMN DATABASE" (Employees/Stats-KPI/Asset+expiry/เอกสารสแกนจริง, ต้อง login ID/Pass, มี PII)
- แนะนำ Supabase ไปแล้ว (Postgres+Auth+Storage, free tier พอใช้ตอนนี้, Pro $25/mo ถ้าโต) — ยังไม่ตัดสินใจ/ยังไม่เริ่มสร้าง
- ถ้า session หน้าคุยเรื่องนี้ต่อ: นี่เป็น infra decision ข้าม repo (พาดพิง PII → ต้องเป็น DA เป็นคน design schema ก่อน ไม่ใช่ UI agent ทำเอง)

### ✅ Done (2026-09-08)
- ย้าย working copy: OneDrive → `C:\Repos\RMN-eBidding-Workflow` ตามคำตัดสิน DA · OneDrive clone = retired ห้าม commit/push จากที่นั่นอีก
- เขียน § UI Rules + § STATUS values ลงไฟล์นี้ (commit 6afecce) — เป็น SoT ของ 2 หัวข้อนี้แล้ว (DA 2a152a0)
- อัปเดต § Working folder: connect `C:\Repos` แล้ว (Marx ทำให้ 2026-09-08) · OneDrive path ขึ้นสถานะ retired ในเอกสาร
- 🐛 fix quick-status ขาด `WITHDRAWN` — L2245 เพิ่ม `<option value="${STATUS.WITHDRAWN}">🟣 ห้างขอยกเลิก</option>`
  - audit 7 จุดแล้ว: WITHDRAWN มีครบทุกจุดอยู่ก่อนแล้ว (CONFIG.STATUS L957 · STATUS_MIGRATE L1024 · `<option>` 3 ชุด L758/792/883 · badge map L1142 + L1518 · section title L1621/1724/2540 · `.b-withdrawn` L188/L53 + `.sd-withdrawn` L278) — ขาดที่ quick-status ที่เดียว
  - ไม่แตะค่า STATUS · ไม่แตะ data logic · `node --check` ผ่าน · 2674 → 2675 บรรทัด
- **merge `:root` 2 บล็อก → เหลือบล็อกเดียวที่ L10** (คำตัดสิน DA ทางเลือก A · มติ King Marx 09-08)
  - ยกค่าที่ชนะจริงจาก L280 ขึ้น L10: `--pill-bg` `#eeece6`→`#f1f3f9` · `--pill-active` `var(--accent)`→`#2b3990` · `--card-border` `#eae8e2`→`#e5e9f2`
  - ย้ายตัวที่มีเฉพาะ L280 ขึ้นมาครบ 7: `--navy` `--navy-dk` `--kpi-blue-1` `--kpi-blue-2` `--kpi-green-1` `--kpi-green-2` `--status-new`
  - ลบบล็อก `:root` ที่ L280 ทั้งบล็อก · คงคอมเมนต์ "Report tab (G-Lead style)" ไว้กับ CSS ที่เหลือ
  - ไม่แตะ `html.dark` · ไม่แก้ pill กลับเป็นส้ม (King Marx สั่งคงน้ำเงิน `#2b3990`)
  - verify: `grep -c ':root{'` = 1 · ไม่มีตัวแปรซ้ำใน `:root` · `node --check` ผ่าน 3 block · 2675 → 2673 บรรทัด · หน้าตา light/dark ไม่ขยับ (computed value เดิมทุกตัว)
- **archive session log** → `WRK_UIUX_ARCHIVE_2569H2.md` (Done ก่อน 2026-09-08) · WRK_UIUX.md 21,099 → ~14.6 KB (ต่ำกว่าเพดาน 20 KB) · ไม่ยุบ § UI Rules / § STATUS values

## 🎨 UI Rules (current — ตรวจจากโค้ดจริง 2026-09-08)
> ของเดิมใน `EBIDDING.md` ถูกครอบ ⛔ แล้ว (M4RX-B4SE a98adeb) — ไฟล์นี้คือฉบับจริง

**Theme**
- Light เป็น default · persist ที่ `localStorage['rmn_theme']` (`'light'` เมื่อไม่เคยตั้ง) · dark = `html.dark`
- Toggle 2 ตัวคุมค่าเดียวกัน: ปุ่ม `#theme-btn` (editor) + switch `#vt-chk` (viewer) — `toggleTheme()` อัปเดตทั้งคู่ ห้ามแยก state
- ห้าม hardcode สีในคอมโพเนนต์ ใช้ CSS var — **ยกเว้น** ราคายื่น / เลขที่ / ชื่อหน่วยงาน / badge สถานะ ที่ต้อง contrast ชัดเสมอ ใช้ hex ตายตัว ห้ามพึ่ง role tint var [[feedback_widget_contrast]]
- ✅ ไฟล์มี `:root` **บล็อกเดียว** (L10) ตั้งแต่ 2026-09-08 — บล็อกที่ 2 ที่ L280 ถูก merge ขึ้นมาแล้ว (คำตัดสิน DA ทางเลือก A) · **แก้ token ทุกตัวที่ L10 ที่เดียว**
  - `--pill-active` = `#2b3990` (navy ไม่ใช่ส้มแบรนด์ `--accent`) — **ตั้งใจ** มติ King Marx 09-08 ห้ามแก้กลับเป็นส้มโดยไม่มีคำสั่งแยก
  - dark mode: `html.dark` specificity (0,1,1) > `:root` (0,1,0) → override ทุกกรณีไม่ว่าลำดับไหน · token ที่ `html.dark` ไม่ประกาศ (`--kpi-*` `--status-new`) ตกมาจาก `:root` ตามเดิม
  - ⛔ ห้ามเพิ่ม `:root` บล็อกที่ 2 อีก — ซ้อนเงียบ debug ยาก

**View mode (mobile / คนดูอย่างเดียว)**
- Editor = ไม่มี query param · Viewer = `?view=1` → `VIEW_MODE` + `body.view-mode`
- `[data-edit-only]` ถูก `display:none !important` (L524) — ปุ่ม Share/Export, tab Records, tab Add Bid, ปุ่มลบ/แก้/quick-status
- **Mobile viewport lock** — ใน view mode เท่านั้น เขียนทับ meta viewport เป็น `maximum-scale=1.0, user-scalable=no` (L928-930) กัน zoom เพี้ยนบนมือถือ · ห้ามใส่ค่านี้ใน meta ตั้งต้น (L5) เพราะ editor ต้อง zoom ได้
- Tab label ย่อเฉพาะ view mode: `dashboard → 📊 ภาพรวม` · `report → 📋 โครงการ` (L933-940)
- `copyViewLink()` (L2658) เติม `view=1` ให้เอง — เป็นทางเดียวที่ใช้แชร์

**Quick-status controls** (`data-action="quickstatus"`)
- `<select>` ในการ์ดแต่ละใบของ tab Records (L2236) · ซ่อนอัตโนมัติใน view mode (อยู่ใน `actionsHtml` ที่เป็น `''` เมื่อ VIEW_MODE)
- Event delegation ที่ `#records-list` `change` (L2616) → `Store.updateStatus()` → `renderTable()` + `renderDash()` ผ่าน rAF (กัน re-render ซ้อน)
- `value` = ค่า STATUS จริง · label สั้นมีอิโมจิ (พื้นที่แคบ) — เปลี่ยน label ได้ เปลี่ยน value ไม่ได้
- ครบ 8 สถานะแล้ว (เพิ่ม `WITHDRAWN` 2026-09-08 — เดิมมี 7 คีย์ผิดได้เงียบๆ)

**Component conventions**
- KPI card: accent เป็น `border-left:3px solid` เท่านั้น (`.kpi-card.blue/green/purple/orange` L313-316) ห้ามใช้ bg เต็มใบ
- Filter: `.pill` ทรงแคปซูล · active = `--pill-active` พื้นทึบ ตัวหนังสือขาว
- ปุ่มขยาย/ดูเพิ่ม = **text-link** (`.expand-btn` L597: ไม่มี bg ไม่มี border) — ปุ่ม "ดูทั้งหมด" ของ competitor (L1932) ใช้แนวเดียวกัน
- Entity tag / pill เล็ก ใช้ `--tag-bg` (L21 / L34) ห้ามใส่ `rgba(255,255,255,…)` ตรงๆ เพราะหายไปใน light mode
- Checklist ทุกชนิดต้องมี interactive HTML widget คู่กับ docx เสมอ [[feedback_checklist_as_widget]]

**Doc Fee UI**
- ซ่อนทั้งหมดแล้ว (`display:none`) ตั้งแต่ 2026-08-31 — workflow จ่ายพร้อมยื่นประมูล · ห้าม unhide เองโดยไม่มีคำสั่ง [[project_docfee_ui_retired]]

## 📋 STATUS values (current — `CONFIG.STATUS` L946-958)
`Object.freeze` · **ค่าที่เก็บใน record คือ string ภาษาไทยเต็ม ไม่ใช่ key** → เปลี่ยน string = ข้อมูล 635 records หลุดทันที

**8 ค่า active**

| key | value (string จริงใน data) | ใช้ที่ |
|---|---|---|
| `WIN_PENDING` | `รอผลพิจารณา [ เป็นผู้เสนอต่ำที่สุด ]` | default ของ Add Bid · fallback ทุกกรณีที่ match ไม่ได้ |
| `LOSE_PENDING` | `รอผลพิจารณา [ ไม่ได้เป็นผู้เสนอต่ำที่สุด ]` | |
| `WINNER` | `อนุมัติสั่งจ้าง/ประกาศให้เป็นผู้ชนะ` | นับเป็น "ชนะ" ใน SME/วงเงิน |
| `CONTRACT` | `จัดทำสัญญาแล้ว` | นับเป็น "ชนะ" ใน SME/วงเงิน |
| `LOSE` | `แพ้ เนื่องจากไม่ได้เสนอราคาต่ำที่สุด` | |
| `DISQUALIFIED` | `แพ้ เนื่องจากโดนปรับตก` | **display อย่างเดียวเรียก "แพ้ ขาดคุณสมบัติ / ถูกปรับตก"** — ห้ามแก้ value |
| `CANCELLED` | `หน่วยงานประกาศยกเลิกโครงการ` | |
| `WITHDRAWN` | `ห้างขอยกเลิกสัญญา` | ไม่มีใน quick-status select |

**3 ค่า legacy** (โค้ดยังรองรับ อ่านได้ แต่ห้ามเขียนใหม่)

| key | value | ปลายทาง |
|---|---|---|
| `PENDING` | `อยู่ระหว่างพิจารณาผล` | มี branch รับใน renderTable → map เป็น `win-pending` |
| `WIN_PRICE` | `ราคาต่ำสุด` | `STATUS_MIGRATE` → `WIN_PENDING` |
| `LOSE_PRICE` | `ราคาไม่ต่ำสุด` | `STATUS_MIGRATE` → `LOSE_PENDING` |

**`STATUS_MIGRATE`** (L1015-1025) แปลงค่าเก่าตอนโหลดจาก localStorage ทุกครั้ง — ครอบคลุมค่ารุ่นก่อนอีก 6 แบบ (`รอผลพิจารณา / …`, `แพ้การประมูล`, `แพ้เนื่องจากขาดคุณสมบัติ/เอกสารไม่สมบูรณ์`, `ยกเลิกโครงการ`, `ห้างขอยกเลิกเอง`)
→ **เพิ่ม/เปลี่ยนชื่อสถานะเมื่อไหร่ ต้องเพิ่มบรรทัดใน `STATUS_MIGRATE` ด้วยเสมอ** ไม่งั้น record เก่าตกไป fallback เงียบๆ

**จุดที่ต้องแก้พร้อมกันเมื่อเพิ่มสถานะใหม่** (7 จุด)
`CONFIG.STATUS` · `STATUS_MIGRATE` · `<option>` 3 ชุด (rpt-status / fstatus / f-status) · quick-status select · badge map (`statusBadge`) · section-title ternary 3 จุด · `.sd-*` / `.b-*` CSS class

## 🚫 Out of Scope
- seed_bids.js / data logic / API calls
- assets.json / personnel.json / doc_fees.json (ข้อมูล — DA/Fee Payment Agent ดูแล)
- TaskCreate / AskUserQuestion

## 📁 Files I touch
- `rmn_ebidding_tracker_2.html` (primary)
- `seed_bids.js` (data typo fixes only)
- `WRK_AGENTS/WRK_UIUX.md` (session log — ตัวนี้)

## 📂 Working folder ที่ต้อง connect
- ✅ **`C:\Repos`** — connect ตัวนี้ตัวเดียว (2026-09-08) · repo อยู่ที่ `C:\Repos\RMN-eBidding-Workflow` มี tracker + WRK_AGENTS/ + seed_bids.js + assets.json/doc_fees.json (fetched, read-only ฝั่งฉัน)
  - ใน `device_bash` mount เป็น `$HOME/mnt/Repos/RMN-eBidding-Workflow`
  - PowerShell/git ใช้ `$r="C:\Repos\RMN-eBidding-Workflow"` — path นี้ **ไม่ได้อยู่ใต้ `$env:USERPROFILE`** เป็นข้อยกเว้นของกฎ no-hardcode-path (repo ย้ายออกจาก OneDrive แล้ว)
- ⛔ **`OneDrive\Claude\Projects\RMN-eBidding-Workflow` = retired** — DA สั่งเลิกใช้ · ห้าม commit/push จาก path นี้อีก ถ้ายัง mount ค้างอยู่ให้ข้ามไป
- ไม่ต้องใช้ `C:\Repos\RMN-eBidding-KB` (private repo, personnel.json) — UI agent ไม่ควรแตะ PII เลย · `C:\Repos\M4RX-B4SE` ก็ไม่ต้อง (KB ต้นฉบับ DA ดูแล)

## ⚙️ My Rules
- Diff/changelog only — ห้าม output full file
- grep/Read หา section ก่อน — ห้าม Read ทั้งไฟล์รวด
- คำนวณ context ก่อน Edit — ถ้าไม่พอ แจ้ง user
- Verify end-of-file + line count หลัง Edit ทุกครั้ง (ป้องกัน truncation)
- Git commit+push เองผ่าน Windows-MCP PowerShell (ลบ .git/HEAD.lock, .git/index.lock ก่อนทุกครั้ง) — ห้ามส่ง git command ให้ user รัน [[feedback_git_push_format]]
- ก่อน commit เช็ค `git status` เสมอ — ถ้ามีไฟล์อื่นค้าง (ไม่ใช่ไฟล์ที่ฉันแก้) ห้ามแตะ/commit รวม เดี๋ยว agent อื่นเสียงาน (พบเคสจริง 2026-08-25: `.gitignore` + `WRK_MAPMAKER.md` ค้างจาก Mapmaker agent ระหว่าง session นี้ — ข้ามไป ไม่ยุ่ง)
