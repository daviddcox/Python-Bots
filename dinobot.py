import pydirectinput as pd
import time
from PIL import ImageGrab, ImageOps
import numpy


def automate():
    global duration
    global run
    image = ImageGrab.grab(box)
    gray_image = ImageOps.grayscale(image)
    a = numpy.array(gray_image.getcolors())
    if a.sum() != 1247 and a.sum() != 1043 and run:
        pd.press('space')
    duration += 1


dino = (670, 480)
pd.keyDown('alt')
pd.press('tab')
pd.keyUp('alt')
time.sleep(.5)
pd.press('space')
duration = 0
run = True
time.sleep(.5)
while True:
    increase = duration/100
    dino = (dino[0], dino[1])
    box = (dino[0], dino[1], dino[0] + 100, dino[1] + 10)
    automate()
