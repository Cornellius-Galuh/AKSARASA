# 🚀 Deploy Aksarasa ke Vercel (GRATIS & MUDAH!)

Vercel adalah platform terbaik untuk deploy aplikasi fullstack (frontend + backend) dalam **1 platform**.

---

## ✅ Keuntungan Vercel:

- ✅ **Deploy frontend & backend sekaligus** (tidak perlu 2 platform)
- ✅ **100% GRATIS** untuk personal projects
- ✅ **Auto SSL/HTTPS** 
- ✅ **Global CDN** (loading super cepat)
- ✅ **Auto deploy** setiap push ke GitHub
- ✅ **No cold start** (tidak sleep seperti Render)
- ✅ **Custom domain gratis**

---

## 📋 Langkah Deploy ke Vercel

### 1️⃣ Persiapan (5 menit)

#### A. Pastikan sudah push ke GitHub
```bash
cd "d:\AKSARASA WIN\LOMBA2"
git add .
git commit -m "Ready for Vercel deployment"
git push origin main
```

#### B. Daftar Akun Vercel (GRATIS)
1. Buka: https://vercel.com/signup
2. Pilih **"Continue with GitHub"**
3. Login dengan akun GitHub Anda
4. Authorize Vercel

---

### 2️⃣ Deploy Aplikasi (3 menit)

#### A. Import Project
1. Di Vercel Dashboard, klik **"Add New..."** → **"Project"**
2. Pilih repository **"AKSARASA"** dari GitHub
3. Klik **"Import"**

#### B. Konfigurasi Project
```
Framework Preset: Other
Root Directory: ./
Build Command: (kosongkan atau "echo 'No build'")
Output Directory: frontend
Install Command: pip install -r backend/requirements.txt
```

#### C. Environment Variables
Klik **"Environment Variables"**, tambahkan:

| Key | Value |
|-----|-------|
| `GEMINI_API_KEY` | `<paste-api-key-anda>` |

Dapatkan API key di: https://makersuite.google.com/app/apikey

#### D. Deploy!
1. Klik **"Deploy"**
2. Tunggu ~2-3 menit
3. Selesai! ✅

---

### 3️⃣ Dapatkan URL Aplikasi

Setelah deploy selesai, Vercel akan memberikan URL seperti:
```
https://aksarasa.vercel.app
```

atau

```
https://aksarasa-xxx123.vercel.app
```

**Aplikasi Anda sudah online dan bisa diakses publik!** 🎉

---

## 🔧 Custom Domain (OPSIONAL)

### Ubah Nama Project
1. Di Vercel Dashboard → Project Settings
2. Klik **"Domains"**
3. Tambahkan domain custom (jika punya) atau edit vercel subdomain:
   - Ketik: `aksarasa-museum` 
   - URL jadi: `https://aksarasa-museum.vercel.app`

---

## 📱 Test Aplikasi

1. Buka URL Vercel Anda
2. Test scan barcode (MUSEUM001, MUSEUM002, dst)
3. Test chat dengan AI
4. Test audio guide

---

## 🔄 Update Aplikasi

Setiap kali ada perubahan code:

```bash
# 1. Edit file yang diperlukan
# 2. Commit & push
git add .
git commit -m "Update fitur baru"
git push

# 3. Vercel akan auto-deploy! (30 detik)
```

---

## 🆚 Vercel vs Render.com

| Fitur | Vercel | Render.com |
|-------|--------|------------|
| **Harga** | GRATIS | GRATIS |
| **Setup** | 1 platform | 2 platform (Netlify + Render) |
| **Cold Start** | ❌ Tidak ada | ⚠️ ~30 detik |
| **Global CDN** | ✅ Ya | ❌ Tidak |
| **Auto Deploy** | ✅ Ya | ✅ Ya |
| **Custom Domain** | ✅ Gratis | ⚠️ Paid only |
| **Serverless Functions** | ✅ Ya | ⚠️ Terbatas |

**Rekomendasi: Vercel lebih mudah dan performa lebih baik!** 🚀

---

## ⚠️ Catatan Penting Vercel

### Batasan Free Plan:
- **Bandwidth**: 100GB/bulan (cukup untuk ribuan visitor)
- **Serverless Function Execution**: 100GB-hours/bulan
- **Function Duration**: Max 10 detik per request (cukup untuk chatbot)

### Jika Function Timeout:
Audio generation (TTS) kadang lambat. Jika error, coba:
1. Reduce audio quality di `server.py`
2. Atau gunakan audio pre-generated
3. Atau upgrade ke Pro plan ($20/bulan)

---

## 🆘 Troubleshooting

### Error: "Module not found"
**Solusi**: Pastikan `backend/requirements.txt` lengkap
```bash
cd backend
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update requirements"
git push
```

### Error: "Function timeout"
**Solusi**: TTS generation terlalu lama. Vercel free plan limit 10 detik.
- Matikan TTS untuk sementara, atau
- Pre-generate audio files

### Error: "API key not configured"
**Solusi**: 
1. Vercel Dashboard → Project → Settings → Environment Variables
2. Pastikan `GEMINI_API_KEY` sudah di-set
3. Redeploy: Deployments → ... → Redeploy

---

## 📋 Checklist Deploy Vercel

- [ ] Code sudah di-push ke GitHub
- [ ] Akun Vercel sudah dibuat & connected ke GitHub
- [ ] Import project AKSARASA ke Vercel
- [ ] Set Environment Variable `GEMINI_API_KEY`
- [ ] Deploy berhasil (tunggu ~2-3 menit)
- [ ] Test aplikasi di URL Vercel
- [ ] Test scan barcode
- [ ] Test chat AI
- [ ] Share link ke teman! 🎉

---

## 💰 Biaya

### GRATIS SELAMANYA untuk:
- Personal projects
- Unlimited websites
- 100GB bandwidth/bulan
- Auto SSL
- Global CDN

### Upgrade (OPSIONAL):
- **Pro**: $20/bulan untuk team collaboration & unlimited bandwidth

---

## 🎯 Kesimpulan

**Vercel adalah pilihan TERBAIK untuk Aksarasa karena:**
1. ✅ Deploy frontend + backend dalam 1 platform
2. ✅ Tidak ada cold start (always fast)
3. ✅ Auto deploy dari GitHub
4. ✅ 100% GRATIS
5. ✅ Setup super mudah (~5 menit)

---

**Selamat! Aplikasi museum Anda siap diakses dunia!** 🌍🎉

**URL:** `https://aksarasa.vercel.app` (ganti dengan URL Anda)
