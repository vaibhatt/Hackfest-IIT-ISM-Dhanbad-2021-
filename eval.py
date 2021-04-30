from PIL import Image
import requests
from io import BytesIO
from utils import *
from tensorflow.keras.preprocessing.sequence import pad_sequences
from caption_model import caption_model
import numpy as np
import pickle
from process_data import *
from gtts import gTTS
import os
import time

idxtoword = pickle.load(open(r"Image_captioning\saved\word indexes\idxtoword.pkl","rb"))
wordtoidx = pickle.load(open(r"Image_captioning\saved\word indexes\wordtoidx.pkl","rb"))


def generateCaption(img_path):
    response = requests.get(img_path)
    img = Image.open(BytesIO(response.content))
    img.load()
    img = encodeImage(img).reshape((1, OUTPUT_DIM))
    in_text = START
    for i in range(max_length):
        sequence = [wordtoidx[w] for w in in_text.split() if w in wordtoidx]
        sequence = pad_sequences([sequence], maxlen=max_length)
        yhat = caption_model.predict([img,sequence], verbose=0)
        yhat = np.argmax(yhat)
        word = idxtoword[yhat]
        in_text += ' ' + word
        if word == STOP:
            break
    final = in_text.split()
    final = final[1:-1]
    final = ' '.join(final)
    return final

def text_to_sound(mytext,output_path):
    myobj = gTTS(text=mytext, lang=text_to_sound_lang, slow=False)
    myobj.save(output_path)

def play_sound(sound_path):
    os.system(sound_path)

def captionize(img_path,output_path,play_now = False,print_caption = False):
    cap = generateCaption(img_path)
    text_to_sound(cap,output_path)

    if(play_now):
        play_sound(output_path)
    start=time.time()
    cur=time.time()
    while cur-start<=2.5:
        cur=time.time()
    if (print_caption):
        print(cap)


