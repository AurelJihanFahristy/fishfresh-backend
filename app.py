import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from routes.predict_routes import predict_bp
from config import Config

root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, static_folder=root_folder, static_url_path='')
CORS(app)

app.config['UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = Config.MAX_CONTENT_LENGTH

os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)

app.register_blueprint(predict_bp)

@app.route('/')
def home():
    return "FishFresh Backend is running!"

# ======================================================================
# PERBAIKAN: Taruh penentuan port di luar blok __main__ agar Gunicorn bisa baca
# ======================================================================
port = int(os.environ.get('PORT', 10000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=False)
