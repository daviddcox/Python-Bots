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


def press(ser: serial.Serial, s: str, duration: float = .05):
    ser.write(s.encode())
    time.sleep(duration)


def press_two(ser: serial.Serial, s: str, s2: str, duration: float = .05):
    ser.write(s.encode())
    ser.write(s2.encode())
    time.sleep(duration)


class Thread_B(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        with serial.Serial('COM4') as ser:
            while True:
                global freq
                print(freq)
                freq1 = freq
                if 755 < freq1 < 790:
                    press(ser, 'A')
                elif 1010 < freq1 < 1040:
                    press(ser, 'X')
                elif 640 < freq1 < 660:
                    press(ser, 'a')
                elif 560 < freq1 < 595:
                    press(ser, 's')
                elif 680 < freq1 < 705:
                    press(ser, 'd')
                elif 850 < freq1 < 890:
                    press(ser, 'B')
                elif 800 < freq1 < 830:
                    press(ser, 'u')
                elif 910 < freq1 < 930:
                    press(ser, 'k')
                elif 960 < freq1 < 980:
                    press(ser, 'h')
                elif 515 < freq1 < 535:
                    press(ser, 'j')
                elif 720 < freq1 < 740:
                    press(ser, 'w')
                else:
                    ser.write(b'0')
                    time.sleep(.075)


a = Thread_A("myThread_name_A")
b = Thread_B("myThread_name_B")

b.start()
a.start()

a.join()
b.join()
