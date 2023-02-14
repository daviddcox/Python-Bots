from multiprocessing import Process
import pyautogui as pt
import pydirectinput as pd
import time

moveForward = True


def func1():
    global moveForward
    while moveForward:
        pd.keyDown('w')
        pd.keyDown('shift')


def func2():
    global moveForward
    while True:
        if pt.locateOnScreen('C:/Users/allen/Pictures/light0.jpg', confidence=.9) is None:
            moveForward = False
            pd.keyUp('shift')
            pd.keyUp('w')
            pd.mouseUp()
            move('s', 2)
            break


if __name__ == '__main__':
    pd.keyDown('alt')
    pd.press('tab')
    pd.keyUp('alt')
    pd.press('esc')
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()

