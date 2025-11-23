from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import google.generativeai as genai
from dotenv import load_dotenv
import logging
from gtts import gTTS
import uuid
import tempfile

# =========================
# Konfigurasi Awal
# =========================
load_dotenv()

# Logging setup - untuk Vercel gunakan stdout
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Flask app dengan folder statis untuk audio
app = Flask(__name__, static_url_path='/static', static_folder='static')
CORS(app, resources={r"/*": {"origins": "*"}})

# =========================
# Inisialisasi Gemini API
# =========================
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-2.0-flash")
    print("✅ Gemini API key loaded successfully!")
else:
    model = None
    print("❌ WARNING: GEMINI_API_KEY not found in .env file")

# =========================
# ROUTES
# =========================
@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "Museum AI Backend Server",
        "api_configured": bool(GEMINI_API_KEY)
    })


@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        # Validate request data
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400
            
        data = request.json
        user_message = data.get('message', '').strip()
        language = data.get('language', 'id')

        # Validate inputs
        if not user_message:
            return jsonify({"error": "Message is required"}), 400
        if not model:
            return jsonify({"error": "API key not configured"}), 500

        # Create system prompt
        system_prompt = f"""
You are Musi, a friendly and smart museum mascot.
Answer in {'Indonesian' if language == 'id' else 'English'}.
Keep responses friendly, concise, and use emojis when appropriate.

Question: {user_message}
Answer:
"""
        # Generate AI response
        try:
            response = model.generate_content(system_prompt)
            ai_response = response.text.strip()
        except Exception as e:
            logging.error(f"Gemini API error: {str(e)}")
            return jsonify({"error": "Failed to generate response"}), 500

        # Generate audio response
        try:
            audio_filename = f"audio_{uuid.uuid4().hex}.mp3"
            audio_folder = os.path.join("static", "audio")
            os.makedirs(audio_folder, exist_ok=True)
            
            tts = gTTS(ai_response, lang="id" if language == "id" else "en")
            audio_path = os.path.join(audio_folder, audio_filename)
            tts.save(audio_path)
            
            return jsonify({
                "success": True,
                "response": ai_response,
                "audio_url": f"/static/audio/{audio_filename}"
            })
        except Exception as e:
            logging.error(f"TTS error: {str(e)}")
            # Continue without audio if TTS fails
            return jsonify({
                "success": True,
                "response": ai_response
            })

        # # Log interaction
        # logging.info(f"User ({language}): {user_message}")
        # logging.info(f"AI: {ai_response}")

        # return jsonify({
        #     "success": True,
        #     "response": ai_response,
        #     "audio_url": f"/static/audio/{audio_filename}" if audio_filename else None
        # })

    except Exception as e:
        logging.error(f"General error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500


@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "api_ready": bool(model)})


# =========================
# Jalankan Server
# =========================
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("=" * 50)
    print("Museum AI Backend Server")
    print("=" * 50)
    print(f"Server running on port {port}")
    print("=" * 50)
    app.run(debug=False, port=port, host='0.0.0.0')
