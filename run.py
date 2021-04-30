import requests
from io import BytesIO
from eval import captionize
import matplotlib.pyplot as plt
from PIL import Image
import time

if __name__=='__main__':
    root="https://github.com/vaibhatt/Hackfest-IIT-ISM-Dhanbad-2021-/blob/master/TEST_IMAGES/"
    urls = [root + "1.jpg?raw=true", root + "2.jpg?raw=true", root + "3.jpg?raw=true", root + "4.jpg?raw=true",
            root + "5.jpg?raw=true", root + "6.jpg?raw=true", root + "7.jpg?raw=true", root + "8.jpg?raw=true",
            root + "9.jpg?raw=true", root + "10.jpg?raw=true"]
    output_path = r"output_path\ouput.mp3"
    for url in urls:
        captionize(url, output_path, play_now=True, print_caption=True)

