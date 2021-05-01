from flask import Flask, render_template, request, Response, redirect

import os

from eval import captionize
from utils import *

app = Flask(__name__)

img_name = "a.jpg"
input_path = r"/home/xori/github/hackathons/Hackfest-IIT-ISM-Dhanbad-2021-/static/a.jpg"
output_path = r"/home/xori/github/hackathons/Hackfest-IIT-ISM-Dhanbad-2021-/static/output.mp3"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api', methods=['GET', 'POST'])
def api():
    if(request.method == 'POST'):
        f = request.files['img']
        f.save("static/a.jpg")

        captionize(input_path, output_path, play_now=False,
                   print_caption=True, url=False)

        return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True)
