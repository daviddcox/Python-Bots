import pyautogui as pt

pt.keyDown('alt')
pt.press('tab')
pt.keyUp('alt')
while True:
    pt.scroll(-1)
