from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import google.generativeai as genai
from dotenv import load_dotenv
import logging
from gtts import gTTS
import uuid
import tempfile
import base64
from io import BytesIO

# Load environment
load_dotenv()

# Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Flask app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    model = None

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
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400
            
        data = request.json
        user_message = data.get('message', '').strip()
        language = data.get('language', 'id')

        if not user_message:
            return jsonify({"error": "Message is required"}), 400
        if not model:
            return jsonify({"error": "API key not configured"}), 500

        # System prompt
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

        # Generate audio (simplified for Vercel - base64 encoded)
        try:
            tts = gTTS(ai_response, lang="id" if language == "id" else "en")
            audio_buffer = BytesIO()
            tts.write_to_fp(audio_buffer)
            audio_buffer.seek(0)
            audio_base64 = base64.b64encode(audio_buffer.read()).decode('utf-8')
            
            return jsonify({
                "success": True,
                "response": ai_response,
                "audio_base64": audio_base64
            })
        except Exception as e:
            logging.error(f"TTS error: {str(e)}")
            return jsonify({
                "success": True,
                "response": ai_response
            })

    except Exception as e:
        logging.error(f"General error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "api_ready": bool(model)})

# For Vercel serverless
if __name__ != '__main__':
    # This is for Vercel
    handler = app
