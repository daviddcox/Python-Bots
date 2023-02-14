import pydirectinput as pd
import keyboard
import threading

run = False


class Check(threading.Thread):
    global run
    if keyboard.read_key() == "r":
        run = True
    elif keyboard.read_key() == "e":
        run = False


class Main(threading.Thread):
    global run
    while run:
        pd.press("z")


if __name__ == "__main__":
    a = Main()
    b = Check()

    a.start()
    b.start()

    a.join()
    b.join()
