import requests
from io import BytesIO
from eval import captionize
import matplotlib.pyplot as plt
from PIL import Image
import time
import urllib
import cv2
import numpy as np
import urllib.request
from PIL import Image
import os
output_path = r"C:\Users\Desktop\NST\OBJECT_DETECTION\ouput.mp3"

if __name__=='__main__':

    #DOWNLOAD IP WEBCAM APP, THEN TO THE LAST LINE OF THE FIRST PAGE, THAT IS START SERVER, then open the IP adress being displayed on the bottom of the screen onto a laptop and/or any other device
    #connected to the SAME NETWORK AS THE PHONE(VERY IMP), ON OPENING THE IP ADDRESS ON THE LAPTOP YOU WILL BE PROMPTED WITH A WHOLE LOT OF TABS AND FEATURES. GO TO THE JAVASCRIPT TAB TO SEE THE LIVE FEED
    # FROM UR PHONE CAMERA, COPY THE IMAGE ADDRESS BY RIGHT-CLICKING ONTO THE LIVE FEED AND THEN SELECTING, 'COPY IMAGE ADDRESS'
    #OPEN THE OBTAINED IMAGE ADDRESS INTO A NEW TAB , STRIP EVERYTHING AFTER .JPG, RELOAD THE PAGE.NOW YOU CAN SEE THE MOST RESENT IMAGE BEING CAPTURED BY THE CAMERA OF MOBILE PHONE.
    #PASTE THAT IMAGE ADDRESS INTO THE URL VARIABLE DEFINED BELOW AND ENJOY THE REST.THATS IT!!

    url='http://192.168.1.13:8080/shot.jpg'
    while True:
        with urllib.request.urlopen(url) as u:
            s = u.read()
            # I'm guessing this would output the html source code ?
        img=np.array(bytearray(s),dtype=np.uint8)
        img=cv2.imdecode(img,-1)
        cv2.imshow("IMAGE",img)
        f=0;
        #INSTRUCTIONS FOR USING OEPNCV INTERFACE
        # 1- PRESS SPACE BAR TO HOLD THE VIDEO AND SEE THE MOST RECENT IMAGE BEING FED AND DECIDE WHETER OR NOT TO GENERATE CAPTIONS FOR THEM OR NOT
        # 2- PRESS EITHER ONE OF THE SPACEBAR,Q OR S KEYS AFTER THIS. PRESSING ANY OTHER KEY WILL TERMINATE THE WINDOW
        #       A) ON PRESSING SPACEBAR, THE STALLED VIDEO WILL AGAIN START STREAMING, AND YOU CAN RETHINK UR IMAGE CHOICE
        #       B) ON PRESSING Q, PROGRAM WILL END.QUIT!!
        #       C) ON PRESSING S, THE OUTPUT OF THE CODE WILL BE GENRATED AND PLAYED. THEN THE VIDEO WILL CONTINUE ITS STREAM
        while cv2.waitKey(2)==ord(' '):
            x=cv2.waitKey(0)
            if x==ord(' '):
                break
            elif x==ord('q'):
                f=1
                exit(0)

            elif x==ord('s'):
                img = Image.fromarray(img)
                captionize(img, output_path, True, True)
                os.remove(output_path)
                break
            else:
                print("WRING KEY PRESSED,TERMINATING!!!")
                f=1
                break
        if f==1:
            break










