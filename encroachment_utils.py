
import numpy as np
from PIL import Image

def preprocess_image(image):
    image = image.resize((128, 128)).convert("RGB")
    return np.array(image).flatten().reshape(1, -1)
