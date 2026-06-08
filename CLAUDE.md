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
> GitHub Pages deploy จาก branch `main` — push ธรรมดาได้เลย

## 🎨 UI Rules
- Light mode default · Viewer URL: `?view=1` (mobile) · Editor: no param (desktop)
- View mode: ซ่อน data-edit-only, theme btn, ปรับ tab labels สั้น
- KPI border-left accent · filter inputs pill-shape · expand btn = text-link

## 📋 STATUS values
รอผลพิจารณา/เป็นผู้เสนอต่ำสุด · ไม่ได้เป็นผู้เสนอต่ำสุด · อนุมัติสั่งจ้าง · จัดทำสัญญา · แพ้การประมูล · แพ้/ขาดคุณสมบัติ · ยกเลิกโครงการ · ห้างขอยกเลิก

## 🤖 Agents
| Agent | MD | หน้าที่ |
|---|---|---|
| E-Bidding Operating | `CLAUDE.md` (tracker) | รับข้อมูลประมูล → seed_bids → git push |
| Map Maker | `MAPMAKER.md` | PDF แผนที่เส้นทางขนส่ง |
| Document Fee Payment | `CLAUDE_FEE_PAYMENT.md` | PDF ใบแจ้งชำระเงิน + email |

## 🔄 Session State (2026-05-29)
### ✅ Done
- seq 92: แพ้การประมูล ✅
- seq 94-98: added + midPrice/lowest ✅
- seq 99-100: parsed, รอผล

### ⏳ Pending
- รอผล 99-100 → อัปเดต status + midPrice (tracker agent)
- light mode toggle + timeline load-more (dev agent)
- FIX 7 (phase 2): one-off structural styles (dev agent)
