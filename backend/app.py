from flask import Flask, send_from_directory
from flask_cors import CORS
import os

from routes.predict_routes import predict_bp
from config import Config

# ✅ FIX: Root proyek adalah 2 level di atas app.py (Fish/backend/app.py -> Fish/)
root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, static_folder=root_folder, static_url_path='')
CORS(app)

# Konfigurasi dari Config class
app.config['UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = Config.MAX_CONTENT_LENGTH

# Pastikan folder uploads ada
os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)

# Register Blueprint
app.register_blueprint(predict_bp)

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def serve_frontend(path):
    full_path = os.path.join(root_folder, path)
    if os.path.exists(full_path):
        return app.send_static_file(path)
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)