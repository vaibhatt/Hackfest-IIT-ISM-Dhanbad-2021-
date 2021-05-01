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

output_path = r"output_path\output.mp3"
input_path = r"E:\Projects\Hackfest_IIT_ISM_2021\input_path\input.jpg"
video_url = 'http://192.168.1.3:8080/video?x.mjpeg'

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

CaptureNPredict(img_path = input_path, sound_path = output_path ,server_address = video_url)