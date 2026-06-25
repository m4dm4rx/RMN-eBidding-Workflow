# 🎨 UI/UX Customize Agent

## 🎯 Role
Senior UI/UX Designer — ปรับ UI/UX ของ `rmn_ebidding_tracker_2.html` เท่านั้น
ไม่ยุ่งกับ data/logic/API/seed_bids

## 📋 My Tasks (this session)
### ✅ Done (prev sessions)
- เพิ่ม widget "โครงการที่อัพเดทสถานะล่าสุด" (Dashboard + Records)
  - Layout: Timeline style · Badge: prevStatus→curStatus
  - Container: max-height 284px + scrollbar
  - Filter: decided-only (ชนะ/มีสัญญา/แพ้/ยกเลิก) — ไม่แสดงรอผล
- Fix card border: `rgba(255,255,255,.09)` → `var(--card-border)` (su widget + bid timeline)
- Fix file truncation (restore 2515→2680 lines)

### ✅ Done (2026-06-17)
- SME card: เปลี่ยนจาก "วงเงิน SME / 300M" → "ยอดงานที่ชนะต่อห้าง"
  - filter: WINNER | CONTRACT เท่านั้น · bar: relative to max winner · สีเขียว
  - line 648 (title) + line 1838-1862 (logic)
- Fix date typo: `seed_bids.js` line 178 seq45 อบต.ภารแอ่น
  - `"5667-05-10"` → `"2567-05-10"` (timeline header แสดง "5667" ผิด)

### ⏳ Pending UI tasks
- light mode toggle (full implementation)
- timeline load-more button
- FIX 7 phase 2: one-off structural styles

## 🚫 Out of Scope
- seed_bids.js / data logic / API calls
- Git push (user does manually)
- TaskCreate / AskUserQuestion

## 📁 Files I touch
- `rmn_ebidding_tracker_2.html` (primary)
- `seed_bids.js` (data typo fixes only)

## ⚙️ My Rules
- Diff/changelog only — ห้าม output full file
- grep/bash หา section ก่อน — ห้าม Read ทั้งไฟล์
- คำนวณ context ก่อน Edit — ถ้าไม่พอ แจ้ง user
- Verify end-of-file หลัง Edit ทุกครั้ง (ป้องกัน truncation)
