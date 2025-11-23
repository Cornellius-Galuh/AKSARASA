# 🚀 Deploy Backend ke Railway.app (GRATIS - Tanpa Kartu Kredit!)

Railway.app memberikan **$5 kredit gratis per bulan** untuk hobby projects, dan **TIDAK PERLU kartu kredit**!

---

## ✅ Keuntungan Railway.app:

- ✅ **100% GRATIS** (tidak perlu kartu kredit)
- ✅ **$5 kredit/bulan** (cukup untuk 500+ jam runtime)
- ✅ **No cold start** (tidak sleep)
- ✅ **Auto deploy** dari GitHub
- ✅ **Easy setup** (~3 menit)
- ✅ **PostgreSQL gratis** (jika butuh database nanti)

---

## 📋 Langkah Deploy ke Railway.app

### 1️⃣ Buat Akun Railway (2 menit)

1. Buka: https://railway.app/
2. Klik **"Start a New Project"** atau **"Login with GitHub"**
3. Authorize Railway dengan GitHub
4. **TIDAK PERLU input kartu kredit!** ✅

### 2️⃣ Deploy Backend (3 menit)

#### A. Create New Project
1. Di Railway Dashboard, klik **"New Project"**
2. Pilih **"Deploy from GitHub repo"**
3. Pilih repository **"AKSARASA"**
4. Klik **"Deploy Now"**

#### B. Konfigurasi Environment Variables
1. Klik project yang baru dibuat
2. Klik tab **"Variables"**
3. Tambahkan variable:
   ```
   GEMINI_API_KEY = <paste-api-key-anda>
   PORT = 5000
   ```
4. Klik **"Add"**

#### C. Konfigurasi Build Settings
1. Klik **"Settings"**
2. Di **"Build"** section:
   - Build Command: `pip install -r backend/requirements.txt -r backend/requirements_railway.txt`
   - Start Command: `cd backend && gunicorn server:app --bind 0.0.0.0:$PORT`
3. Root Directory: (kosongkan atau `/`)

#### D. Tunggu Deploy Selesai
- Railway akan otomatis build & deploy (~2-3 menit)
- Setelah selesai, akan muncul **"Deployed"** status

### 3️⃣ Dapatkan URL Backend

1. Di project Railway, klik **"Settings"**
2. Scroll ke **"Domains"** atau **"Public Networking"**
3. Klik **"Generate Domain"**
4. Copy URL yang muncul, contoh:
   ```
   https://aksarasa-backend-production-xxxx.up.railway.app
   ```

### 4️⃣ Update Frontend untuk Gunakan Backend Railway

1. Buka file `frontend/script.js`
2. Update baris ke-4:
   ```javascript
   const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
       ? 'http://127.0.0.1:5000'
       : 'https://aksarasa-backend-production-xxxx.up.railway.app'; // ← Ganti dengan URL Railway Anda
   ```

3. Commit & push:
   ```bash
   git add frontend/script.js
   git commit -m "Update backend URL to Railway"
   git push origin main
   ```

4. Vercel akan auto-deploy frontend dengan URL backend yang baru!

---

## ✅ SELESAI!

Aplikasi Anda sekarang online:
- **Frontend (Vercel)**: `https://aksarasa3.vercel.app`
- **Backend (Railway)**: `https://aksarasa-backend-production-xxxx.up.railway.app`

---

## 💰 Biaya Railway.app

### Free Tier ($5 kredit/bulan):
- **500+ jam runtime** (cukup untuk 1 bulan non-stop!)
- **100GB bandwidth**
- **No cold start** (always online)
- **TIDAK PERLU kartu kredit**

### Jika Kredit Habis:
- Railway akan notify Anda
- Bisa upgrade ke Hobby plan ($5/bulan)
- Atau buat akun baru (email lain)

---

## 🆚 Perbandingan Platform

| Platform | Kartu Kredit? | Cold Start? | Free Limit |
|----------|--------------|-------------|------------|
| **Railway** | ❌ TIDAK | ❌ Tidak | $5/bulan |
| Render | ✅ **PERLU** | ⚠️ 30 detik | 750 jam |
| Vercel | ❌ Tidak | ⚠️ Tidak support Flask | Limited |
| Fly.io | ❌ Tidak | ❌ Tidak | 3 VMs |

**Railway = Pilihan TERBAIK untuk backend Python tanpa kartu!** 🚀

---

## 🔧 Troubleshooting

### Error: Build failed
**Solusi**: 
- Pastikan `backend/requirements.txt` sudah ada
- Pastikan `backend/requirements_railway.txt` sudah ada (berisi gunicorn)

### Error: Application failed to respond
**Solusi**:
- Pastikan start command: `cd backend && gunicorn server:app --bind 0.0.0.0:$PORT`
- Pastikan environment variable `GEMINI_API_KEY` sudah di-set

### Backend timeout saat generate audio
**Normal!** TTS generation kadang lambat. Railway lebih cepat dari Render di free tier.

---

## 📋 Checklist Deploy Railway

- [ ] Akun Railway sudah dibuat (tanpa kartu!)
- [ ] Repository AKSARASA sudah di-import
- [ ] Environment variable `GEMINI_API_KEY` sudah di-set
- [ ] Deploy berhasil
- [ ] Domain Railway sudah di-generate
- [ ] URL backend sudah di-copy
- [ ] File `frontend/script.js` sudah update URL backend
- [ ] Commit & push ke GitHub
- [ ] Test aplikasi di Vercel!

---

**Selamat! Aplikasi fullstack Anda online 100% GRATIS tanpa kartu kredit!** 🎉
