import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # = Fish/backend/

class Config:
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    SPECIES_MODEL_PATH = os.path.join(BASE_DIR, 'models', 'model_spesies_terbaik_final.h5')
    FRESHNESS_MODEL_PATH = os.path.join(BASE_DIR, 'models', 'best_freshness_model.h5')

    SPECIES_CONFIDENCE_THRESHOLD = 0.95
    FRESHNESS_CONFIDENCE_THRESHOLD = 0.60
    KNOWN_SPECIES = ["Horse Mackerel", "Red Sea Bream", "Sea Bass"]
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024