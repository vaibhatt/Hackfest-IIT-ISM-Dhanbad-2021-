from PIL import Image
from utils import *
from tensorflow.keras.preprocessing.sequence import pad_sequences
from caption_model import caption_model
import numpy as np
import pickle
from process_data import encodeImage
from gtts import gTTS   
import os

wordtoidx = pickle.load(open(r"E:\Projects\Hackfest_IIT_ISM_2021\Image_captioning\saved\word indexes\word_to_index","rb"))
idxtoword = pickle.load(open(r"E:\Projects\Hackfest_IIT_ISM_2021\Image_captioning\saved\word indexes\index_to_word","rb"))


def generateCaption(photo):
    in_text = START
    for i in range(max_length):
        sequence = [wordtoidx[w] for w in in_text.split() if w in wordtoidx]
        sequence = pad_sequences([sequence], maxlen=max_length)
        yhat = caption_model.predict([photo,sequence], verbose=0)
        yhat = np.argmax(yhat)
        word = idxtoword[yhat]
        in_text += ' ' + word
        if word == STOP:
            break
    final = in_text.split()
    final = final[1:-1]
    final = ' '.join(final)
    return final


def evaluate(img_path):
    img = Image.open(img_path)
    img.load()
    img = encodeImage(img).reshape((1,OUTPUT_DIM))
    return generateCaption(img)

def text_to_sound(mytext,output_path):
    myobj = gTTS(text=mytext, lang=text_to_sound_lang, slow=False)
    myobj.save(output_path)

def play_sound(sound_path):
    os.system(sound_path)

def captionize(img_path,output_path,play_now = False,print_caption = False):
    cap = evaluate(img_path)
    text_to_sound(cap,output_path)
    if(print_caption):
        print(cap)
    if(play_now):
        play_sound(output_path)

