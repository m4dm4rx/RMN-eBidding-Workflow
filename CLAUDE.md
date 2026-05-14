# RMN e-Bidding Tracker

Web app ติดตามการประมูลโครงการถนน ปีงบประมาณ 2569.

## Files
- `rmn_ebidding_tracker_2.html` — single source of truth (HTML + SEED_BIDS data)
- `netlify/functions/proxy.js` — CORS proxy for opend.data.go.th API
- Live: https://dorpnightmare-wq.github.io/rmn-ebidding-tracker/rmn_ebidding_tracker_2.html
- GitHub: https://github.com/dorpnightmare-wq/rmn-ebidding-tracker.git

## Data entry workflow
1. User pastes row(s) from Excel → Claude **แปลงเป็น text** แสดงข้อมูลที่ parse ได้ (id, name, agency, province, budget, bid, date, status)
2. User ยืนยัน → Claude add to SEED_BIDS in HTML
3. User ยืนยัน push → git push → GitHub Pages auto-deploys

**Excel columns (left→right):**
1. เลขที่โครงการ (id เช่น 69049395087)
2. ชื่อโครงการ (name — long text)
3. หน่วยงาน (agency)
4. จังหวัด (province)
5. งบประมาณ (budget)
6. หมายเหตุ — contains bid after "ยื่น" keyword (เช่น "ยื่น 1,318,000")
7. วันที่/เวลา (date — เช่น "11 พ.ค.69 เวลา 9.00น." → "2569-05-11")
8. (ignore)

**Default values when adding:**
- `entity`: "ห้างหุ้นส่วน RMN"
- `status`: ดูจากผลเบื้องต้นวันประมูล
  - ราคาเราต่ำสุด (ชนะเบื้องต้น) → `"รอผลพิจารณา / เป็นผู้เสนอราคาต่ำสุด"`
  - ราคาเราไม่ต่ำสุด (แพ้เบื้องต้น) → `"รอผลพิจารณา / ไม่ได้เป็นผู้เสนอราคาต่ำสุด"`
- `seq`: next number after last entry
- `pct`: `Math.round((budget - bid) / budget * 10000) / 100` (0 if no budget)

## Git push commands
```
git -C "C:\Users\Advice\OneDrive\Claude\Projects\RMN e-Bidding Tracker" add rmn_ebidding_tracker_2.html
git -C "C:\Users\Advice\OneDrive\Claude\Projects\RMN e-Bidding Tracker" commit -m "Add seq XX: agency date"
git -C "C:\Users\Advice\OneDrive\Claude\Projects\RMN e-Bidding Tracker" push
```

## STATUS values (stored in data)
- รอผลพิจารณา / เป็นผู้เสนอราคาต่ำสุด
- รอผลพิจารณา / ไม่ได้เป็นผู้เสนอราคาต่ำสุด
- อนุมัติสั่งจ้าง/ประกาศให้เป็นผู้ชนะ
- จัดทำสัญญาแล้ว
- แพ้การประมูล
- แพ้เนื่องจากขาดคุณสมบัติ/เอกสารไม่สมบูรณ์
- ยกเลิกโครงการ
- ห้างขอยกเลิกเอง

## Entity options
- ห้างหุ้นส่วน RMN (default)
- กิจการร่วมค้า RMN
- กิจการร่วมค้า ตักสิลา
