from flask import Flask, render_template, request, Response, redirect, url_for

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

app = Flask(__name__)

output_path = r"/home/xori/github/hackathons/Hackfest-IIT-ISM-Dhanbad-2021-/static/output.mp3"
input_path = r"/home/xori/github/hackathons/Hackfest-IIT-ISM-Dhanbad-2021-/static/a.jpg"
video_url = 'http://192.168.1.5:8080/video?x.mjpeg'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api', methods=['GET', 'POST'])
def api():
    
    cap = cv2.VideoCapture(f"{video_url}")
    while True:
        ret,frame = cap.read()
        w,h,l = frame.shape
        dim = (int(w/3),int(h/3))
        #frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow("capturing",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if(request.method == 'POST'):
            cv2.imwrite(input_path,frame)
            captionize(input_path, input_path,play_now=True,print_caption=True)

    cap.release()
    cv2.destroyAllWindows()

    return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True)
