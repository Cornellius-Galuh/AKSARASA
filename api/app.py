from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Import the main app
from backend.server import app as flask_app

# This is required for Vercel
app = flask_app
