import pydirectinput as pt
import pyautogui as pd
import time
import keyboard


def main():
    if input("Mode:") == 1:
        run = True
        pt.keyDown('alt')
        pt.press('tab')
        pt.keyUp('alt')
        while True:
            while run:
                if pd.locateOnScreen('C:/Users/allen/Pictures/bush.jpg', confidence=.7, grayscale=True) is not None:
                    pt.keyDown('left')
                    time.sleep(.5)
                    pt.keyUp('left')
                    pt.keyDown('right')
                    time.sleep(.5)
                    pt.keyUp('right')
                else:
                    time.sleep(10)
                    pt.press('down')
                    pt.press('z')
                    pt.press('right')
                    pt.press('z')
                    while pd.locateOnScreen('C:/Users/allen/Pictures/bush.jpg', grayscale=True, confidence=.7) is None:
                        pt.press('z')
            while not run:
                if keyboard.is_pressed('2'):
                    run = True
    else:
        time.sleep(2)
        while True:
            pt.press("z")


if __name__ == "__main__":
    main()
