import pydirectinput as pt
import pyautogui as pd
import time
import keyboard


def main():
    pt.keyDown('alt')
    pt.press('tab')
    pt.keyUp('alt')
    i = 50
    while i > 0:
        pt.moveTo(610, 535)
        pt.click()
        time.sleep(.1)
        pt.moveTo(950, 700)
        pt.click()
        time.sleep(.1)
        i -= 1


if __name__ == "__main__":
    main()
