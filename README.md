# Aksarasa - Museum Audio Guide 🎨🎭

Aplikasi panduan audio museum interaktif dengan AI chatbot yang dapat diakses melalui scan barcode/QR code pada koleksi museum.

## 🌟 Fitur

- 📱 Scan barcode dengan kamera atau upload gambar
- 🎧 Audio guide otomatis untuk setiap koleksi
- 🤖 AI Chatbot (Gemini) untuk tanya jawab tentang koleksi
- 🌐 Dukungan bahasa Indonesia & English
- 📜 History scan yang tersimpan
- 🎨 UI modern dan responsive

## 🚀 Deploy ke Internet

Aplikasi ini sudah siap untuk di-deploy secara **GRATIS** menggunakan **Vercel**!

**Baca panduan lengkap di [DEPLOYMENT.md](./DEPLOYMENT.md)**

## 💻 Menjalankan Lokal

### Backend
```bash
cd backend
pip install -r requirements.txt
# Buat file .env dengan GEMINI_API_KEY
python server.py
```

### Frontend
Buka `frontend/index.html` di browser atau gunakan Live Server.

## 📁 Struktur Project

```
LOMBA2/
├── backend/
│   ├── server.py              # Flask API server
│   ├── requirements.txt       # Dependencies
│   ├── .env.example          # Template environment variables
│   └── static/audio/         # Generated audio files
├── frontend/
│   ├── index.html            # Main page
│   ├── script.js             # App logic
│   ├── style.css             # Styling
│   └── _redirects            # Netlify redirects
├── scripts/                  # Helper scripts
├── netlify.toml              # Netlify config
├── Procfile                  # Render.com config
├── runtime.txt               # Python version
└── DEPLOYMENT.md             # Panduan deploy lengkap
```

## 🔑 Environment Variables

Buat file `backend/.env`:
```
GEMINI_API_KEY=your_api_key_here
```

Dapatkan API key gratis di: https://makersuite.google.com/app/apikey

## 📦 Dependencies

### Backend
- Flask
- google-generativeai (Gemini AI)
- gTTS (Text-to-Speech)
- flask-cors
- python-dotenv
- gunicorn (untuk production)

### Frontend
- HTML5 QR Code Scanner
- Vanilla JavaScript (no framework)

## 🎯 Museum Collections

Demo collections available:
- MUSEUM001: Wayang Kulit Arjuna
- MUSEUM002: Lukisan Mona Lisa (Replika)
- MUSEUM003: Patung Venus de Milo (Replika)
- MUSEUM004: Keris Pusaka Jawa
- MUSEUM005: Patung Buddha Borobudur

## 🌐 Live Demo

Setelah deploy, aplikasi Anda akan dapat diakses di:
- **URL Vercel**: `https://aksarasa.vercel.app` (ganti dengan URL Anda)

## 📱 Cara Penggunaan

1. Buka aplikasi di smartphone/desktop
2. Klik "Scan dengan Kamera" atau "Upload Gambar"
3. Arahkan ke barcode koleksi museum
4. Dengarkan audio guide otomatis
5. Chat dengan AI untuk bertanya lebih lanjut

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend**: Python, Flask
- **AI**: Google Gemini 1.5 Flash
- **TTS**: Google Text-to-Speech (gTTS)
- **Hosting**: Vercel (Fullstack)

## 📄 License

MIT License - Free to use and modify

## 👥 Credits

Built with ❤️ for museum digitalization

---

**Ready to deploy? Follow [DEPLOYMENT.md](./DEPLOYMENT.md)** 🚀
