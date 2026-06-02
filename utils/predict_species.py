import numpy as np
import tensorflow as tf

from utils.preprocess import preprocess_image
from utils.labels import SPECIES_LABELS
from config import Config

# Load model sekali saat startup
model = tf.keras.models.load_model(
    Config.SPECIES_MODEL_PATH,
    compile=False,
    custom_objects={'InputLayer': tf.keras.layers.InputLayer}
)

def predict_species(img_path):
    processed_image = preprocess_image(img_path)
    prediction = model.predict(processed_image)
    predicted_index = int(np.argmax(prediction))
    confidence = float(np.max(prediction))
    species = SPECIES_LABELS[predicted_index]
    return species, confidence
