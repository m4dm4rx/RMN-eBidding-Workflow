# 🧭 Ecosystem & Datacenter Admin Agent

## 🎯 Task Scope
รับคำสั่งหลัก → dispatch ไป sub-agent ตาม scope → sync Backbone DB


> 📦 session log ก่อน 2026-09-07 ย้ายไป `WRK_ECOSYSTEM_ADMIN_ARCHIVE_2569H2.md` — ไม่ต้องอ่านตอนเปิด session
> 📏 เพดานไฟล์นี้ 20 KB · เกินเมื่อไหร่ตัดท้ายเข้า archive ก่อนเริ่มงานใหม่

## 🔄 Session State (2026-09-07 — DA: naming model + กฎ Raven + จัดระเบียบ working copy)
- ✅ **มติ King Marx — naming model ใหม่** บันทึกแล้ว: `KB § ชั้นยศ` + `KB § 🐦 Raven Mail` · `DESIGN_PRINCIPLES` Decision log 2 แถว · `CLAUDE.md § 📢` 2 บรรทัด (ประกาศในคอมมิตเดียวกันตามหน้าที่ broadcast)
- ✅ artifact `process-map.html` แก้ชื่อกล่อง advisor + แถว ownership → **republish ทับ URL เดิม** (ไม่แตะเนื้อหาอื่นตามที่รับปากใน Raven)
- 🛠️ **พบและแก้: working copy ไม่ตรง origin ทั้ง 2 repo** — `M4RX-B4SE` ค้างบน branch `claude/upbeat-johnson-xdUyN` (1 commit `21cf15d`, **ไม่มี KB_ECOSYSTEM_ADMIN.md / DESIGN_PRINCIPLES.md บนดิสก์เลย**) → `git checkout -B main origin/main` ได้ `ec7af3e` · `RMN-eBidding-Workflow` ช้ากว่า origin **78 commit** → `merge --ff-only` ได้ `c61cfb9` · ⚠️ **ไม่มีข้อมูลหาย** ของครบบน origin/main ทุกไฟล์
- ⚠️ **บทเรียน PowerShell (จดไว้กันซ้ำ):** `$KL = Get-Content $k` — ถ้าใช้ชื่อ `$K` จะ **ทับตัวแปร `$k` ทันที** เพราะ PowerShell ไม่แยกตัวพิมพ์เล็ก/ใหญ่ → path กลายเป็นค่าว่าง เขียนไฟล์ไม่ได้ (เจอจริง 2 รอบ) · ต่อไปตั้งชื่อ array ว่า `$KL/$DL/$CL` เท่านั้น
- ⏸️ **pending approval — ยังไม่บันทึกลงดิสก์ ห้ามถือเป็นกฎ:** architecture Workspace/GitHub/LINE · ownership TAB 1/2/3 · ผู้รับสรุปรายวัน + ผู้มีสิทธิเขียน · guard rails ①–⑩ · ถ้อยคำเส้นแบ่ง advisor (เปิด/ปิด) · TAB 2 `basis_amount` รอคำตอบ Top
- 📌 LINE OA `RMN Finance Capture` **Friends = 1** → office/แม่ ยังไม่เข้าระบบ ยังทดสอบ intake จริงไม่ได้ · สถานะ not operational

## 🔄 Session State (2026-09-07 ต่อ — DA: Finance Capture v1 ส่งมอบ + ย้าย repo ออกจาก OneDrive)
- ✅ **Execution Card RMN Finance Capture v1 ปิดครบ** — `M4RX-B4SE` `8ddaa84` governance (ก่อน) → `1ee1c0f` implementation · `Workflow` `40f8455` broadcast · RC1–RC9 อยู่ในโค้ดจริง · **60 offline tests ผ่านบนเครื่อง** · dependency 0 ตัว · ไม่มี secret ในไฟล์ใด · **หยุดก่อน deploy ตามคำสั่ง**
- 📌 MB1 ปิด: Messaging API channel `RMN Finance Capture` **Channel ID 2011458199** (ID ไม่ใช่ secret บันทึกได้)
- ✅ **ย้าย repo 3 ตัวออกจาก OneDrive → `C:\Repos\`** (path เดียวกันทุกเครื่อง ไม่มีชื่อ user) · `Workflow` `3c44f15` · `M4RX-B4SE` `1d37740`
- 🔴 **OneDrive ทำ git พังจริง 3 แบบในวันเดียว** — บทเรียนที่แพงที่สุดของวันนี้:
  ① `.git/*.lock` ค้าง ลบจาก mount ไม่ได้ → commit ไม่ผ่าน (แก้ชั่วคราวด้วย `mv` ได้ แต่ไม่ควรต้องทำ)
  ② `.git/objects` **ขาด ~60 objects** + reflog เสีย + commit-graph parse ไม่ผ่าน → `RMN-eBidding-Workflow` ต้อง **re-clone ทั้ง repo**
  ③ clone ลงมา **ผิด branch** เพราะ `origin/HEAD` ของ `M4RX-B4SE` ชี้ `claude/upbeat-johnson-xdUyN` (scaffold 1 commit) — หลอกทั้ง DA ตอนบ่ายและ clone ใหม่ตอนดึก · แก้ default branch บน GitHub แล้ว
- ⚠️ **path เดิมผูกชื่อ user** `C:\Users\Advice\OneDrive\...` → เครื่องที่ 2 (`asus`) ใช้ไม่ได้ตั้งแต่ต้น ไม่ใช่เพิ่งพัง
- ⚠️ **บทเรียน git จาก mount**: `device_bash` ลบไฟล์ไม่ได้ทั้ง mount (ไม่ใช่แค่ OneDrive) และ `core.autocrlf` ไม่ตั้งใน VM → ถ้า commit ตรงๆ ไฟล์ CRLF ที่ไม่ได้แตะจะกลายเป็น diff ทั้งไฟล์ · ต้องใส่ `-c core.autocrlf=input` ทุกคำสั่ง · **git ต้องผ่าน PowerShell เท่านั้น กฎเดิมถูกแล้ว**
- ⏸️ **ค้าง 4 ข้อ**
  ① `SKILL.md` ของ scheduled task ยังชี้ OneDrive · อยู่นอก git · `Documents\Claude` ขอสิทธิ์ผ่าน bridge ไม่ได้ → user รันสคริปต์เอง **ทั้ง 2 เครื่อง** (จุดนี้เคยทำ checker พังเงียบเป็นสัปดาห์)
  ② `_old_*` + `.corrupt_20260907` ใน OneDrive — เก็บ 7 วันแล้วลบ
  ③ Q1 Codex deploy GCP ได้จริงไหม — ถ้าไม่ได้ `runbook/RUNBOOK.md` เขียนให้ King Marx ทำเองครบทุกขั้น + rollback
  ④ Q2 แม่/Office เป็นเพื่อน OA + OA เข้ากลุ่มแล้วยัง — **Friends ยัง = 1** daily summary ยังส่งไม่ถึงใคร
- 🔎 **ยังไม่ย้าย ต้องตัดสินแยก** — `BSKNBot\` และ `RMN e-Bidding Tracker\` ยังเป็น repo ใน OneDrive เสี่ยงแบบเดียวกันเป๊ะ
- 📌 **แต่ละ Sir แก้ path ใน WRK ของตัวเอง** — DA แก้ให้ไม่ได้ตามกฎ ownership · ประกาศรายชื่อไฟล์ไว้ใน `CLAUDE.md § 📢` แล้ว · Sir MM ยังมี `WRK_MAPMAKER.md` uncommitted อยู่บนดิสก์ (ไฟล์ไม่หาย แต่ของที่เคย `git add` หายไปกับ object ที่เสีย ต้อง add ใหม่)


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
