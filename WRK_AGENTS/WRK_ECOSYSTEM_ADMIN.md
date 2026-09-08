# 🧭 Ecosystem & Datacenter Admin Agent

## 🎯 Task Scope
รับคำสั่งหลัก → dispatch ไป sub-agent ตาม scope → sync Backbone DB


> 📦 session log ก่อน 2026-09-07 ย้ายไป `WRK_ECOSYSTEM_ADMIN_ARCHIVE_2569H2.md` — ไม่ต้องอ่านตอนเปิด session
> 📏 เพดานไฟล์นี้ 20 KB · เกินเมื่อไหร่ตัดท้ายเข้า archive ก่อนเริ่มงานใหม่

## 📌 Carried forward (ยกมาจาก session 09-07 ที่ย้ายเข้า archive แล้ว — ยังไม่ปิด)
- ⏸️ **pending approval — ยังไม่บันทึกลงดิสก์ ห้ามถือเป็นกฎ**: architecture Workspace/GitHub/LINE · ownership TAB 1/2/3 · ผู้รับสรุปรายวัน + ผู้มีสิทธิเขียน · guard rails ①–⑩ · ถ้อยคำเส้นแบ่ง advisor · TAB 2 `basis_amount` รอคำตอบ Top
- 🔎 **repo ที่ยังอยู่ใน OneDrive ต้องตัดสินแยก**: `BSKNBot\` (อยู่ใต้ `OneDrive\BSKN`) · ~~`RMN e-Bidding Tracker\`~~ **หายจาก OneDrive root แล้ว ยืนยัน 09-08**
- 📌 **Sir MM**: `WRK_MAPMAKER.md` uncommitted บนดิสก์ — ของที่เคย `git add` หายไปกับ object ที่เสีย ต้อง add ใหม่ (เจ้าของทำเอง DA แตะไม่ได้)
- ⚠️ **บทเรียนที่ต้องไม่หาย** ① PowerShell ไม่แยกพิมพ์เล็ก/ใหญ่ — ตั้ง array เป็น `$KL/$DL/$CL` ห้ามใช้ `$K` ทับ `$k` ② commit จาก mount ต้องใส่ `-c core.autocrlf=input` ไม่งั้นไฟล์ CRLF ที่ไม่ได้แตะกลายเป็น diff ทั้งไฟล์

## 🔄 Session State (2026-09-08 — DA: จัดระเบียบ path หลังย้าย repo + รับ EBIDDING.md เข้า ownership)
- ✅ **`SKILL.md` ของ scheduled task 3 ตัวแก้ path → `C:\Repos\...`** (`doc-fee-morning-alert` ไม่ต้องแก้) · ⚠️ ไฟล์อยู่ `%USERPROFILE%\Documents\Claude\Scheduled\` **นอก git และมีแค่บนเครื่อง PC MARX** → เครื่อง `asus` ไม่มีเลย ต้องทำซ้ำเมื่อย้ายเครื่อง
- ✅ **registry**: `KB § scheduled tasks` บันทึก path ใหม่ครบ 4 task + ความเปราะที่ผูกกับเครื่องเดียว (`M4RX-B4SE 6360954`)
- ✅ **รับ `EBIDDING.md` เข้า Ownership Matrix + ติดป้าย ⚠️ HISTORICAL + ครอบ ⛔ 3 ส่วนที่ชี้ path ผิด** (`§ Files & URLs` · `§ Multi-Machine` · `§ Git Push`) — **ไม่ลบเนื้อหาเดิม เก็บเป็นหลักฐาน** (`M4RX-B4SE 33bc8b2`)
- 🔴 **ผมนับผิดเอง** — รายงานว่าเจอ scheduled task "ตัวที่ 5" แต่ registry ถูกอยู่แล้วที่ 4 ตัว (นับ `doc-fee-morning-alert` ซ้ำ) · บันทึกเป็นความผิดของผมใน `DESIGN_PRINCIPLES` Decision log
- ⚠️ **commit 2 ตัวมี BOM ในหัวข้อ** (`9c93cff`, `6360954`) เพราะ `Set-Content -Encoding UTF8` เขียน BOM → ต่อไปใช้ `New-Object Text.UTF8Encoding $false` เท่านั้น · แก้ย้อนหลังได้แต่ต้อง force-push **ยังไม่ทำ รอคำสั่ง**
- 📌 **archive รอบนี้** ย้าย session `09-04` + `09-05` (94 บรรทัด) เข้า `WRK_ECOSYSTEM_ADMIN_ARCHIVE_2569H2.md` เพราะไฟล์ชน `20,453 / 20,480 B` เหลือ 27 B · **ตัดท้ายเข้า archive ไม่ขยายเพดาน**
- ⏸️ **ค้างต่อ** ① Raven ให้ Sir UI/UX ยืนยัน `EBIDDING.md § UI Rules` + `§ STATUS values` ยังตรงกับ tracker ไหม (**ต้องให้ King Marx เป็นคนส่ง**) ② Q1 Codex deploy GCP ได้จริงไหม ③ Q2 แม่/Office เป็นเพื่อน OA + OA เข้ากลุ่ม (**Friends ยัง = 1**) ④ deploy Finance Capture รออนุมัติแยก ⑤ `_old_*` + `.corrupt_20260907` ครบ 7 วันแล้วลบ ⑥ `BSKN-Expense_Bot-LINE` ahead 3 + dirty 4 ไฟล์ — King Marx ย้ายเอง ⑦ `Company-Assets/` + `KB_DOC_EXPIRY.md` ยังไม่มีเจ้าของใน git


## 🔄 Session State (2026-09-08 ต่อ — DA: ปิด 3 สำเนา UI/STATUS + รับ infra Finance Capture เข้าทะเบียน)
- ✅ **มติ Lord COMMANDER ทางเลือก A** → ครอบ `⛔` เหนือ `EBIDDING.md § UI Rules` + `§ STATUS values` พร้อมเหตุผลในบรรทัดถัดไป (`M4RX-B4SE a98adeb`) · **ทั้งไฟล์ = ประวัติศาสตร์ 100% ทุก section ถูกครอบครบ ไม่ลบอะไรเลย**
- ✅ **Sir UI ส่ง `6afecce`** — `WRK_UIUX.md` 89→151 บรรทัด มี `§ UI Rules` + `§ STATUS values` ของจริง (8 active + 3 legacy `PENDING`/`WIN_PRICE`/`LOSE_PRICE` + `STATUS_MIGRATE` + checklist 7 จุด) verify จากโค้ด tracker ไม่ใช่จากความจำ
- ✅ **ปิดปัญหาข้อมูลเดียวกันอยู่ 3 ที่** — `CLAUDE.md § UI Rules/STATUS` ถอดข้อความออกเหลือแค่ป้ายชี้ไป `WRK_UIUX.md` · ข้อความรุ่นก่อนย้ายเข้า `CLAUDE_ARCHIVE_2569H1.md` ไม่ลบ (`Workflow 2a152a0`) · Ownership Matrix + Decision log (`M4RX-B4SE f7ac222`)
- 📏 **archive 2 รอบวันนี้** `WRK_ECOSYSTEM_ADMIN.md` 20,453→10,341 B (ย้าย 09-04+09-05 ออก 94 บรรทัด `Workflow 99367c8`) · `CLAUDE.md` 20,366→19,540 B (ย้ายประกาศที่ปิดเรื่องแล้ว 2 ข้อ) — **ตัดท้ายเข้า archive ไม่ขยายเพดานทั้ง 2 ครั้ง**
- ⚔️ **คำตัดสิน repo path** — clone ใน OneDrive = **retired ห้าม commit/push จากที่นั่น** · `6afecce` ที่ push จาก OneDrive ไม่ต้องแก้ย้อนหลัง DA ff เข้า `C:\Repos` แล้ว · **รอ King Marx connect `C:\Repos\RMN-eBidding-Workflow` ให้ session Sir UI**
- ✅ **infra Finance Capture เข้าทะเบียน** — project `rmn-finance-capture` org `rmngroup.net` · SA `rmn-finance-capture-runtime@...` · Drive `Evidence`/`Daily Exports`/`_Trash` · Sheet `RMN Finance Capture [backend]` · secret 2 ตัวยังไม่มี version (`M4RX-B4SE 2987bc5` + `16fe209`)
- 🔴 **ผมตรวจ infra จริงเทียบ runbook แล้วพบว่า runbook ของผมผิด 3 จุด ไม่ใช่ infra ผิด** ① ชื่อ (`Exports/`→`Daily Exports/` · `RMN Finance Ledger`→`RMN Finance Capture [backend]`) ② **สั่งสร้างโฟลเดอร์ย่อยตามประเภทใน `Evidence/` ทั้งที่โค้ด upload เข้า `EVIDENCE_FOLDER_ID` ตรงๆ** → ลบคำสั่งออก ③ ไม่ระบุว่า `Daily Exports/` ต้องมี Editor ด้วย (daily job copy Sheet เข้าไป) · เพิ่ม gate ตรวจ header row + seed `CATEGORIES` ก่อน deploy
- ⏸️ **blocker ก่อน deploy (ยังไม่ปิด)** B1 header row 4 tab ตรงตัวอักษร+ลำดับ (ผิด 1 ช่อง = ยอดลงคอลัมน์ผิดเงียบๆ) · B2 seed `CATEGORIES` 6 ค่า · B3 เปิด API `run`/`cloudbuild`/`artifactregistry`/`cloudscheduler`/`monitoring` · B4 ใส่ค่า secret · B5 GATE ปิด OA auto-reply · B6 groupId/userId จริงจาก signed event · B7 Friends ยัง = 1
- ⏸️ **ค้างที่ต้องให้ King Marx เดิน** ① connect `C:\Repos` ให้ Sir UI ② Raven ให้ Sir UI เขียน `WRK_UIUX.md` ต่อ + แก้ `quick-status` ที่ขาด `WITHDRAWN` (7/8 = คีย์ผิดเงียบ) ③ `:root` 2 บล็อกใน tracker — DA ขอรายชื่อตัวแปรซ้ำก่อนตัดสิน ④ deploy Finance Capture รออนุมัติแยกใบ ⑤ `_old_*`+`.corrupt_20260907` ครบ 7 วันแล้วลบ ⑥ `BSKN-Expense_Bot-LINE` ahead 3 + dirty 4

## 🔄 Session State (2026-09-08 ต่อ 2 — DA: รับ Raven ตอบ 3 checks + ปิดเคสชื่อไฟล์ OneDrive)
- 🦅 **รับ Raven `Lord COMMANDER of GPT` — Finance Capture infra review (verification response · no deploy)** ① header row 4 tab **ยังไม่เช็ค/ยังไม่ยืนยัน** (work report ยืนยันแค่ว่ามี 4 tab ชื่อตรง ไม่ได้รายงาน field/ลำดับ) ② `CATEGORIES` seed **ถือว่า 0 / not confirmed** จนตรวจจริง ③ SA Editor บน `_Trash/` + `Daily Exports/` = **confirmed by inheritance** จาก parent `RMN Finance Capture` แต่ต้อง verify permission บน child folder จริงก่อน production
- ⚔️ **เลข ①②③ ของ COMMANDER ≠ B1-B7 ของ DA** — ③ = permission inheritance (ตรงกับ runbook ผิดข้อ ③) **ไม่ใช่ B3 = เปิด API 5 ตัว** · ห้าม agent ใดอ่านว่า B3 ปิดแล้ว
- ✅ **ลำดับที่อนุมัติ**: ปิด B1 + B2 → verify B3-permission (child folder) → **แล้วค่อย** เปิด API 5 ตัว · **ยัง NO-GO deploy** ทุกกรณี
- 🔴 **DA ทำ B1/B2 จาก session Claude ไม่ได้** — connector Google Drive ที่ต่ออยู่ผูก `dorpnightmare@gmail.com` · ค้น `title contains 'RMN Finance Capture'` = **ไม่เจอ** (Sheet อยู่ org `rmngroup.net` คนละบัญชี) → **King Marx ต้องเปิด Sheet เอง** ตั้ง header 4 tab + seed `CATEGORIES` 6 ค่า ตาม field list ใน runbook
- ✅ **ปิดเคสชื่อไฟล์ซ้ำ OneDrive** — `[EGP]_E-BIDDING…DATABASE` 1,531 ไฟล์ `.md/.html/.js/.json` = 0 ไม่ชนกับ repo · OneDrive root **ไม่มี `RMN e-Bidding Tracker` แล้ว** (ยืนยัน `EBIDDING.md:30-32` ชี้ path ตาย) · `Ai Agents Cloud BASE\` = **เจ้าของ Codex / Technical Execution** ชื่อไฟล์คนละชุด ไม่ใช่สำเนา `WRK_AGENTS\` (มติ King Marx 09-08)
- ✅ **ค้างข้อ ②③ ของบล็อกก่อนปิดเอง** — Sir UI ทำเสร็จแล้วใน `WRK_UIUX.md` (`6afecce`+) ② quick-status เพิ่ม `WITHDRAWN` L2245 audit ครบ 7 จุด ③ `:root` ซ้ำ 3 ตัว `--pill-bg` · `--pill-active` · `--card-border` — **L280 ชนะทั้งแอปใน light mode** (dark ไม่โดน) · **ยังไม่ merge บล็อก รอ DA ตัดสิน**
- 🦅 **Raven รอบ 2 จาก Lord COMMANDER (09-08) — verification alignment** ✅ รับ correction เลขข้อแล้ว (`①②③` ≠ `B1-B7`) · **B3 = APIs 5 ตัว ยัง OPEN** · **รับ `B8` = verify permission child folder จริง เข้าทะเบียน blocker**
- 📌 **B1 SoT = `Finance-Capture/runbook/RUNBOOK.md` L98-113** (work report ฝั่ง COMMANDER ไม่มี field list ให้เทียบ) · ตรวจแล้ว runbook มี header 4 tab ครบ + `CATEGORIES` 6 ค่าตรงกับที่ COMMANDER ระบุทุกตัว → **ไม่มี gap ไม่ต้องแก้ runbook**
- 🔐 **กฎใหม่ — data boundary** ⛔ ห้าม share Sheet/Drive เข้า Gmail ส่วนตัวหรือ connector Claude เพื่อความสะดวก · B1+B2 ให้ King Marx ทำใน Workspace ตรงๆ (ประกาศลง `CLAUDE.md § 📢` แล้ว)
- ✅ **gate ปิด blocker = read-back** — B1 ตั้ง header เสร็จต้องอ่านกลับเทียบตัวอักษร+ลำดับ · B2 seed เสร็จต้องอ่านกลับนับให้ได้ 6 · ไม่รับ inheritance/report เป็นหลักฐาน
- 📋 **สถานะปัจจุบัน B1-B8 = OPEN ทั้งหมด** · ลำดับ: ① Marx ตั้ง header + seed → ② verify child permission → ③ เปิด API 5 ตัว → ④ secret/LINE gate/signed IDs/Friends → ⑤ deploy ขออนุมัติแยกใบ · **NO-GO deploy · ห้ามแตะ LINE · ห้ามใส่ secret**
- 📏 **archive รอบ 3 (09-08)** `CLAUDE.md` 20,106→**18,433 B** (เหลือ 2,047 B ถึงเพดาน) — ย้ายประกาศปิดเรื่องแล้ว 3 ข้อเข้า `CLAUDE_ARCHIVE_2569H1.md § ประกาศที่ย้ายมาเก็บ (09-08 รอบ 2)`: ① PII เบอร์ติดต่อ (SoT `KB § Rule 19`) ② Git Close-out (SoT `CLAUDE.md § 🔀 Git Push` ในไฟล์เดิม) ③ UI Rules/STATUS (SoT `WRK_UIUX.md` · ป้ายชี้ `§ 🎨` ยังอยู่) · **ไม่ลบ section ที่เป็นกฎ ไม่ขยายเพดาน**
- 📏 **archive รอบ 4 (09-08)** ไฟล์นี้ 19,950→**14,624 B** — ย้าย session `09-07` + `09-07 ต่อ` เข้า `WRK_ECOSYSTEM_ADMIN_ARCHIVE_2569H2.md` · **ก่อนย้ายกลั่นของที่ยังไม่ปิดขึ้นเป็น `§ 📌 Carried forward`** (pending approval 6 ข้อ · `BSKNBot\` ใน OneDrive · Sir MM uncommitted · บทเรียน PowerShell `$K` + `core.autocrlf=input`) — **ไม่ทิ้งงานค้างลง archive**
