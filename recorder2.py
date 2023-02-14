from __future__ import annotations
import pydirectinput as pd
import recorder
import threading
import serial
import time
freq = 0


class Thread_A(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        tuner = recorder.Tuner()
        global freq
        while True:
            freq = tuner.run()


class Thread_B(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        moves = ("w", "a", "s", "d")
        while True:
            global freq
            freq1 = freq
            if 700 < freq1 < 710:
                for i in range(len(moves)):
                    if moves[i] == "w":
                        pd.keyDown("w")
                    else:
                        pd.keyUp(moves[i])
            elif 710 < freq1 < 720:
                for i in range(len(moves)):
                    if moves[i] == "a":
                        pd.keyDown("a")
                    else:
                        pd.keyUp(moves[i])
            elif 720 < freq1 < 730:
                for i in range(len(moves)):
                    if moves[i] == "s":
                        pd.keyDown("s")
                    else:
                        pd.keyUp(moves[i])
            elif 730 < freq1 < 740:
                for i in range(len(moves)):
                    if moves[i] == "d":
                        pd.keyDown("d")
                    else:
                        pd.keyUp(moves[i])
            else:
                for i in range(len(moves)):
                    pd.keyUp(moves[i])


a = Thread_A("myThread_name_A")
b = Thread_B("myThread_name_B")

b.start()
a.start()

a.join()
b.join()
