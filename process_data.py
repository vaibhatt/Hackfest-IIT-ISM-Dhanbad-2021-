from utils import *
from PIL import Image
import numpy as np
import tensorflow.keras.preprocessing.image
import tensorflow
from model import preprocess_input
from model import encode_model

def encodeImage(img):
  img = img.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
  x = tensorflow.keras.preprocessing.image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  x = preprocess_input(x)
  x = encode_model.predict(x) 
  x = np.reshape(x, OUTPUT_DIM )
  return x