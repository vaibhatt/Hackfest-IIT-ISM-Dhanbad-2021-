from eval import captionize
from utils import *

img_name = "1.jpg"
input_path = "https://github.com/vaibhatt/Hackfest-IIT-ISM-Dhanbad-2021-/blob/67ff354a6635c0d79e4858af63af70133bb844e7/TEST_IMAGES/10.jpg?raw=true"
output_path = r"/home/xori/github/hackathons/Hackfest-IIT-ISM-Dhanbad-2021-/output_path/output.mp3"


if __name__ == '__main__':
    captionize(input_path, output_path, play_now=True,
               print_caption=True, url=True)
