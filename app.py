from flask import Flask, render_template, request, Response, redirect, url_for

from eval import captionize
from capture import CaptureNPredict
from utils import *

app = Flask(__name__)

output_path = r"output_path\output.mp3"
input_path = r"E:\Projects\Hackfest_IIT_ISM_2021\input_path\input.jpg"
video_url = 'http://192.168.1.3:8080/video?x.mjpeg'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api', methods=['GET', 'POST'])
def api():
    if(request.method == 'POST'):

        CaptureNPredict(img_path = input_path, sound_path = output_path ,server_address = video_url)

        return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True)
