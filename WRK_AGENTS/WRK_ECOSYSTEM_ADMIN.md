# 🧭 Ecosystem & Datacenter Admin Agent

## 🎯 Task Scope
รับคำสั่งหลัก → dispatch ไป sub-agent ตาม scope → sync Backbone DB


> 📦 session log ก่อน 2026-09-07 ย้ายไป `WRK_ECOSYSTEM_ADMIN_ARCHIVE_2569H2.md` — ไม่ต้องอ่านตอนเปิด session
> 📏 เพดานไฟล์นี้ 20 KB · เกินเมื่อไหร่ตัดท้ายเข้า archive ก่อนเริ่มงานใหม่

## 📌 Carried forward (ยกมาจาก session 09-07 ที่ย้ายเข้า archive แล้ว — ยังไม่ปิด)
- 💰 **Finance Capture — B1 ✅ B2 ✅ (read-back 09-08) · B3-B8 OPEN 6 ข้อ** · ลำดับที่ตกลง: **B8 verify permission child folder → B3 เปิด API 5 ตัว → B4 secret → B5 GATE ปิด OA auto-reply → B6 groupId/userId → B7 Friends** · SoT ของ header/seed = `Finance-Capture/runbook/RUNBOOK.md` L98-113 · ⛔ **NO-GO deploy** ต้องขออนุมัติแยกใบ
- ⚠️ **B8 ตรวจ 2 ทิศ**: ① SA `rmn-finance-capture-runtime@` = Editor บน Sheet + `Evidence/` + `_Trash/` + `Daily Exports/` ② **แม่/Office = Viewer เฉพาะ `Evidence/` + `Daily Exports/` ห้ามเห็น `_Trash/` และ Sheet** · ต้องระบุว่าสิทธิ์ **explicit หรือ inherited** ไม่รับคำว่า "เข้าถึงได้"
- 🔴 **09-09 · แก้ไข B8 scope — LINE user ≠ Workspace user** (correction จาก Lord COMMANDER of GPT, ยืนยัน King Marx) — B8 = ตรวจสิทธิ์ Drive/Sheet เท่านั้น **ไม่ใช่เงื่อนไขสิทธิ์ใช้ chatbot** · Office ใช้ LINE ผ่านกลุ่มที่ได้รับอนุญาตได้โดยไม่ต้องมี Workspace account · **Workspace target users**: Marx (Super Admin เทคนิค) · แม่ (Owner/Billing) · Wanida (target user — **ยังไม่ยืนยันการสร้าง account** → บันทึกสถานะ "Workspace access pending — account not yet verified" ห้ามสมมติ identity หรือ block bot runtime เพราะเหตุนี้) · สิทธิ์ Workspace ที่ตั้งใจ: `RMN Finance Capture [backend]` + `_Trash` = runtime SA เท่านั้น (ห้าม share แม่/Wanida เพื่อความสะดวก) · `Evidence`/`Exports`/`Daily Exports` = แม่ Viewer
- 📌 **dirty ค้างของจริง 2 ตัว** `M WRK_AGENTS/WRK_MAPMAKER.md` (**Sir MM**) · `?? build_taksila_letterhead.py` (**Codex** provisional) · **`BSKN-Expense_Bot-LINE` = `E:\WEB APP\...` พักไว้ diverged โดยตั้งใจ** เจ้าของ King Marx · checker ไม่ต้องฟ้อง
- ⏸️ **deploy Finance Capture = ต้องขออนุมัติแยกใบ** ไม่รวมกับใบไหนทั้งสิ้น (ยืนยันร่วม DA + Lord COMMANDER 09-08)
- ⏸️ **`_old_*` + `.corrupt_20260907` ใน OneDrive** — ครบ 7 วันวันที่ **09-14** แล้วลบได้
- ⏸️ **Q1 (จากบล็อก 09-08 แรก) ยังไม่มีคำตอบ**: Codex deploy GCP ได้จริงไหม — ถ้าไม่ได้ `RUNBOOK.md` ต้องเขียนให้ King Marx ทำเองครบทุกขั้น + rollback (ตอนนี้ Marx เดิน B1/B2 เองแล้ว แต่ยังไม่มีมติปิดข้อนี้)
- ⚠️ **BOM ใน 2 commit เก่า** (`9c93cff`, `6360954`) จาก `Set-Content -Encoding UTF8` — แก้ย้อนหลังต้อง force-push **ยังไม่ทำ รอคำสั่ง** · ต่อไปใช้ `New-Object Text.UTF8Encoding $false` เท่านั้น
- ⏸️ **pending approval — ยังไม่บันทึกลงดิสก์ ห้ามถือเป็นกฎ**: architecture Workspace/GitHub/LINE · ownership TAB 1/2/3 · ผู้รับสรุปรายวัน + ผู้มีสิทธิเขียน · guard rails ①–⑩ · ถ้อยคำเส้นแบ่ง advisor · TAB 2 `basis_amount` รอคำตอบ Top
- 🔎 **repo ที่ยังอยู่ใน OneDrive ต้องตัดสินแยก**: `BSKNBot\` (อยู่ใต้ `OneDrive\BSKN`) · ~~`RMN e-Bidding Tracker\`~~ **หายจาก OneDrive root แล้ว ยืนยัน 09-08**
- 📌 **Sir MM**: `WRK_MAPMAKER.md` uncommitted บนดิสก์ — ของที่เคย `git add` หายไปกับ object ที่เสีย ต้อง add ใหม่ (เจ้าของทำเอง DA แตะไม่ได้)
- ⚠️ **บทเรียนที่ต้องไม่หาย** ① PowerShell ไม่แยกพิมพ์เล็ก/ใหญ่ — ตั้ง array เป็น `$KL/$DL/$CL` ห้ามใช้ `$K` ทับ `$k` ② commit จาก mount ต้องใส่ `-c core.autocrlf=input` ไม่งั้นไฟล์ CRLF ที่ไม่ได้แตะกลายเป็น diff ทั้งไฟล์


- 📧 **เจอ root cause จริงของ `gmail-bid-auto-update` — Claude ต่อ Gmail ผิดบัญชี** (DA เขียนผิดมา 2 รอบก่อนหน้า ทั้งคู่เป็นข้อสรุปจากกล่องที่ว่างเปล่า) · e-GP **ส่งเมลมาตลอดและถี่มาก** จาก **`process@gprocurement.go.th`** — `แจ้งผลการจัดซื้อจัดจ้าง (เลขที่โครงการ …)` · `แจ้งการตรวจรับงาน` · `ยกเลิกการแจ้งการตรวจรับงาน` · `สัญญา/ใบสั่งซื้อสั่งจ้างฉบับลงนาม` · `ลงนามในสัญญาฯ` (ยืนยันจากภาพกล่องเมลจริงของ King Marx: วันนี้ 2 ฉบับ · จันทร์ 3 · ศุกร์-พฤหัส-1/2 ก.ย. อีกเพียบ)
- 🔴 **กล่องที่รับเมล e-GP จริง = กล่องของแม่ ไม่ใช่ของ Marx** (ยืนยัน King Marx 09-08) · บัญชีที่ Claude connector ต่ออยู่ = `dorpnightmare@gmail.com` → ค้น `from:process@gprocurement.go.th` (รวม spam+trash) = **0 ฉบับ** · ค้น `แจ้งผลการจัดซื้อจัดจ้าง`/`ตรวจรับงาน` = **0 ฉบับ** → **checker ตัวเก่าไม่เคยพัง มันไปเฝ้ากล่องที่ไม่มีเมลตั้งแต่แรก**
- ⏸️ **ทางแก้ — ต้องเลือกก่อนสร้าง watcher ใหม่** ✅ **แนะนำ:** ตั้ง **filter + forward ในกล่องแม่** เงื่อนไขแคบ `from:process@gprocurement.go.th` → ส่งต่อเข้ากล่อง Marx (แม่ยังได้รับครบเหมือนเดิม · Gmail ต้องกดยืนยันปลายทาง 1 ครั้ง) · ทางเลือกรอง: เปลี่ยนอีเมลที่ผูกกับบัญชี e-GP เป็นของ Marx (⚠️ แม่จะไม่ได้รับต่อ ต้องถามก่อน) · ⛔ **ห้ามต่อ Gmail connector เข้ากล่องแม่โดยตรง** — กล่องนั้นมีเมลส่วนตัวของท่านด้วย = ขยาย data boundary เกินจำเป็น ผิดกฎที่ตั้งไว้ 09-08 · ⛔ ห้ามสร้าง watcher จนกว่าเมล `process@` โผล่ในกล่องที่ต่ออยู่จริงอย่างน้อย 1 ฉบับ
- 💡 **มูลค่าที่ได้ถ้าแก้เรื่องนี้** — `แจ้งผลการจัดซื้อจัดจ้าง` มีเลขที่โครงการอยู่ในหัวข้อ = **อัปเดตผลประมูลเข้า tracker อัตโนมัติได้** และรู้ผลแพ้/ชนะโดยไม่ต้องเปิดพอร์ทัลเอง · เป็นงานหลังศุกร์ ไม่ใช่ตอนนี้
- ✅ **แบบแจ้งปัญหา `69081989` ปิดแล้ว** — กรมบัญชีกลางโทรกลับมาแก้ให้วันถัดมา (King Marx ยืนยัน 09-08)

## ⚡ โหมดประหยัดโควตา R1-R6 — **หมดอายุเอง 2026-09-11 16:00** (มติ King Marx + Lord COMMANDER 09-08)
> 🔴 **DA session ใหม่อ่านตรงนี้ก่อนเริ่มงาน** · โควตา weekly เหลือ ~24% ต้องพอถึงศุกร์ · **e-bidding มาก่อนเสมอ** — ประกาศเข้าเมื่อไหร่ก็ได้ มีเดดไลน์จริง (ใบแจ้งชำระ + แผนที่) · ห้ามยืมโควตาส่วนนี้ไปทำ Finance Capture
- **R1** Raven/รายงาน = **delta-only** ตอบเฉพาะที่เปลี่ยน ห้ามทวนบริบทเดิม
- **R2** GPT ร่าง governance text → DA แค่ตรวจ + commit (โอนการพิมพ์ ไม่ใช่โอน ownership)
- **R3** ปิดงานด้วย commit hash ที่ยืนยันแล้ว **ห้ามเปิดไฟล์ verify ซ้ำรอบสอง**
- **R4** เขียน session state **ตอนจบก้อนงานใหญ่เท่านั้น** ไม่เขียนทุกก้อนย่อย
- **R5** archive **เฉพาะไฟล์ที่ชนเพดานจริง** ห้ามทำเชิงป้องกัน
- **R6** ลง `seed_bids.js` / tracker ของประมูลใหม่ → **ทำย้อนหลังเป็นชุดหลังศุกร์ได้** (ไม่มีเดดไลน์) · ที่ต้องทำทันทีมีแค่ PDF ใบแจ้งชำระ + PDF แผนที่
- **default = Sonnet** · เปิด Opus เฉพาะตัดสินที่ผิดแล้วเสียหายจริง · ปิด session เมื่อจบก้อนงาน ห้ามลากยาว
- ⛔ **เส้นแดงห้ามผ่อน**: secret/credential · IAM + เส้นแบ่งข้อมูล (แม่/Office ห้ามเห็น `_Trash/` + Sheet) · ห้าม share Sheet เข้า Gmail ส่วนตัว/connector · production authorization gate · 1 ไฟล์ 1 เจ้าของ · blocker ที่เป็น "โครงสร้าง" ตาม `DESIGN_PRINCIPLES` ข้อ 1️⃣2️⃣
- 📌 **หลังหมดอายุ**: ลบ section นี้ทิ้งทั้งก้อน ไม่ต้องย้ายเข้า archive
