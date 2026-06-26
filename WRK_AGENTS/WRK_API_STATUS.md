# 🔌 Agent: API Status Monitor

## 🎯 Task
ตรวจสอบสถานะ EGP API และ endpoints ที่เกี่ยวข้อง

## 📋 Scope
- Ping `api.egp.go.th` endpoints
- เช็ค Netlify proxy / public CORS proxies
- รายงานผลเฉพาะตอน API กลับมาใช้ได้
- **ไม่แตะ** bid data / HTML / git

## 🔗 Endpoints
| URL | Type |
|---|---|
| `https://api.egp.go.th/api/egp-contract?projectid=` | Primary |
| `https://api.egp.go.th/api/egp-winner?projectid=` | Primary |
| `https://rmn-ebidding-tracker.netlify.app/.netlify/functions/proxy` | Proxy (broken — no function deployed) |
| `https://allorigins.win/get?url=` | Fallback |
| `https://corsproxy.io/?url=` | Fallback |

## 📌 Known Issues
- Netlify proxy URL ใน app เป็น relative `/.netlify/functions/proxy` → resolve ผิดบน GitHub Pages
- `proxy.js` ไม่มีในโฟลเดอร์ — ไม่ได้ deploy
- EGP ตอบ 503 ทุก endpoint (upstream ล่ม ณ 2026-05-29)

## ⏰ Scheduled Task
- ID: `egp-api-status-check`
- ทุก 3 ชม. (`0 */3 * * *`)
- Silent ถ้า 503 / แจ้งเฉพาะตอน ✅
