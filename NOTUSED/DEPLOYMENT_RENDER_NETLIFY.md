# 🚀 Panduan Deploy Aksarasa ke Internet

Aplikasi Aksarasa terdiri dari 2 bagian:
1. **Frontend** (HTML/CSS/JS) → Deploy ke **Netlify** 
2. **Backend** (Python/Flask) → Deploy ke **Render.com** (GRATIS)

---

## 📋 Persiapan

### 1. Buat Akun (GRATIS)
- **Netlify**: https://app.netlify.com/signup
- **Render**: https://dashboard.render.com/register

### 2. Install Git (jika belum ada)
Download dari: https://git-scm.com/downloads

### 3. Push ke GitHub
```bash
cd "d:\AKSARASA WIN\LOMBA2"
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/USERNAME/aksarasa.git
git push -u origin main
```

---

## 🎯 LANGKAH 1: Deploy Backend ke Render.com

### A. Persiapan File Backend
Pastikan file berikut sudah ada (sudah saya buatkan):
- ✅ `Procfile` 
- ✅ `runtime.txt`
- ✅ `backend/requirements.txt`
- ✅ `backend/requirements_production.txt`

### B. Deploy ke Render
1. Login ke https://dashboard.render.com
2. Klik **"New +"** → **"Web Service"**
3. Connect repository GitHub Anda
4. Pilih repository **aksarasa**
5. Konfigurasi:
   ```
   Name: aksarasa-backend
   Region: Singapore (terdekat)
   Branch: main
   Root Directory: backend
   Runtime: Python 3
   Build Command: pip install -r requirements.txt -r requirements_production.txt
   Start Command: gunicorn server:app --bind 0.0.0.0:$PORT
   Instance Type: Free
   ```

6. **Environment Variables** (klik "Add Environment Variable"):
   ```
   GEMINI_API_KEY = <your-gemini-api-key>
   PYTHON_VERSION = 3.11.0
   ```

7. Klik **"Create Web Service"**
8. Tunggu ~5-10 menit sampai deploy selesai
9. **COPY URL backend Anda**, contoh: `https://aksarasa-backend.onrender.com`

### C. Test Backend
Buka di browser: `https://aksarasa-backend.onrender.com/`

Harus muncul:
```json
{
  "status": "online",
  "message": "Museum AI Backend Server",
  "api_configured": true
}
```

---

## 🌐 LANGKAH 2: Deploy Frontend ke Netlify

### A. Update URL Backend di Frontend
1. Buka file `frontend/script.js`
2. Cari baris ke-3, ganti URL backend:
   ```javascript
   const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
       ? 'http://127.0.0.1:5000'
       : 'https://aksarasa-backend.onrender.com'; // ← GANTI INI dengan URL backend Anda
   ```

3. Save dan commit:
   ```bash
   git add frontend/script.js
   git commit -m "Update backend URL untuk production"
   git push
   ```

### B. Deploy ke Netlify

#### Cara 1: Via GitHub (RECOMMENDED)
1. Login ke https://app.netlify.com
2. Klik **"Add new site"** → **"Import an existing project"**
3. Pilih **GitHub** → Pilih repository **aksarasa**
4. Konfigurasi:
   ```
   Branch to deploy: main
   Base directory: (kosongkan)
   Build command: (kosongkan atau echo "No build")
   Publish directory: frontend
   ```
5. Klik **"Deploy site"**
6. Tunggu ~1-2 menit
7. Netlify akan generate URL random, contoh: `https://silly-cupcake-123abc.netlify.app`

#### Cara 2: Via Drag & Drop
1. Login ke https://app.netlify.com
2. Drag & drop folder `frontend` ke area "Want to deploy a new site without connecting to Git?"
3. Tunggu upload selesai
4. Copy URL yang diberikan

### C. Custom Domain (OPSIONAL)
1. Di Netlify Dashboard → **Site settings** → **Domain management**
2. Klik **"Options"** → **"Edit site name"**
3. Ganti nama: `aksarasa-museum` → URL jadi: `https://aksarasa-museum.netlify.app`

---

## ✅ SELESAI! Aplikasi Anda Sudah Online

### URL Anda:
- **Frontend**: `https://your-site-name.netlify.app`
- **Backend**: `https://aksarasa-backend.onrender.com`

---

## 🔧 Troubleshooting

### Problem: Backend error "API key not configured"
**Solusi**: 
- Pastikan sudah set `GEMINI_API_KEY` di Render Environment Variables
- Restart service di Render Dashboard

### Problem: Frontend tidak bisa connect ke backend
**Solusi**:
1. Cek apakah backend URL di `script.js` sudah benar
2. Test backend URL di browser, harus return JSON status
3. Cek CORS - pastikan backend ada `CORS(app, resources={r"/*": {"origins": "*"}})`

### Problem: Render backend sleep setelah 15 menit idle
**Ini normal di Free Plan**. Backend akan otomatis bangun saat ada request (butuh 30-60 detik first load).

**Solusi**: Upgrade ke Paid Plan ($7/bulan) untuk always-on server.

### Problem: Audio tidak muncul
**Solusi**:
- Cek Environment Variable `GEMINI_API_KEY` sudah benar
- Cek logs di Render Dashboard untuk error TTS
- Pastikan package `gTTS` terinstall

---

## 📱 Update Aplikasi Setelah Deploy

Setiap kali ada perubahan code:

```bash
# 1. Edit file yang perlu diubah
# 2. Commit & push
git add .
git commit -m "Deskripsi perubahan"
git push

# 3. Netlify & Render akan auto-deploy otomatis!
```

---

## 💰 Biaya

### GRATIS (Free Tier):
- **Netlify**: 100GB bandwidth/bulan, unlimited sites
- **Render**: 750 jam/bulan (cukup untuk 1 bulan non-stop)

### Batasan Free Tier:
- ⚠️ Backend sleep setelah 15 menit tidak ada traffic
- ⚠️ Cold start ~30-60 detik saat backend bangun

### Upgrade (OPSIONAL):
- **Render Paid**: $7/bulan untuk always-on server
- **Netlify Pro**: $19/bulan untuk analytics & password protection

---

## 🆘 Butuh Bantuan?

1. Cek logs di Render: **Dashboard → Your Service → Logs**
2. Cek logs di Netlify: **Site → Deploys → Deploy log**
3. Test backend API manual di browser atau Postman

---

## 📋 Checklist Deploy

- [ ] Backend di-push ke GitHub
- [ ] Backend deployed ke Render
- [ ] Environment variable `GEMINI_API_KEY` sudah di-set di Render
- [ ] Backend URL sudah di-copy
- [ ] Frontend `script.js` sudah update backend URL
- [ ] Frontend deployed ke Netlify
- [ ] Test scan barcode di frontend
- [ ] Test chat AI di frontend
- [ ] Share URL ke teman/public! 🎉

---

**Selamat! Aplikasi museum Anda sekarang bisa diakses dari mana saja! 🚀🎉**
