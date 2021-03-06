import cv2
from eval import captionize
from utils import *
from PIL import Image
from tensorflow.keras.preprocessing.sequence import pad_sequences
from caption_model import caption_model
import numpy as np
import pickle
from process_data import encodeImage
from gtts import gTTS   
import os
import requests
from io import BytesIO
from PIL import Image, ImageFile

def CaptureNPredict(img_path,sound_path,server_address,play_now = True,print_caption = True,show_video = True):
    cap = cv2.VideoCapture(f"{video_url}")
    while True:
        ret,frame = cap.read()
        w,h,l = frame.shape
        dim = (int(w/3),int(h/3))
        #frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow("capturing",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.waitKey(1) & 0xFF == ord('x'):
            cv2.imwrite(img_path,frame)
            captionize(img_path, sound_path,play_now=True,print_caption=True)

    cap.release()
    cv2.destroyAllWindows()
