import os
from flask import Flask
from flask_cors import CORS
from routes.predict_routes import predict_bp
from config import Config

# Buat inisialisasi Flask seminimal mungkin agar server produksi stabil
app = Flask(__name__)
CORS(app)

# Konfigurasi upload folder
app.config['UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = Config.MAX_CONTENT_LENGTH

# Pastikan folder upload lokal/server siap
os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)

# Daftarkan rute AI Anda
app.register_blueprint(predict_bp)

# Rute utama untuk memastikan backend aktif di internet
@app.route('/')
def home():
    return "FishFresh Backend is running successfully on Render!"

# Setel port dinamis langsung sebagai variabel global yang bisa dibaca Gunicorn
port = int(os.environ.get('PORT', 10000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=False)
