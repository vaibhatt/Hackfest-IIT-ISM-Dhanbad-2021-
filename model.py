from tensorflow.keras.applications.inception_v3 import InceptionV3
import tensorflow.keras.applications.inception_v3
from utils import *
from tensorflow.keras.models import Model



inception_weight_path = r"/home/xori/github/hackathons/Hackfest-IIT-ISM-Dhanbad-2021-/Image_captioning/saved/inception net/inception_v3_weights_tf_dim_ordering_tf_kernels.h5"
if USE_INCEPTION:
  encode_model = InceptionV3(weights = inception_weight_path)
  encode_model = Model(encode_model.input, encode_model.layers[-2].output)
  WIDTH = 299
  HEIGHT = 299
  OUTPUT_DIM = 2048
  preprocess_input = \
    tensorflow.keras.applications.inception_v3.preprocess_input
else:
  encode_model = MobileNet(weights='imagenet',include_top=False)
  WIDTH = 224
  HEIGHT = 224
  OUTPUT_DIM = 50176
  preprocess_input = tensorflow.keras.applications.mobilenet.preprocess_input
