from __future__ import annotations
import time
import keyboard
import serial


def press(ser: serial.Serial, s: str, duration: float = .05):
    ser.write(s.encode())
    time.sleep(duration)
    ser.write(b'0')
    time.sleep(.075)


def main():
    with serial.Serial('COM4') as ser:
        while True:
            if keyboard.read_key() == "w":
                print("you pressed w")
                press(ser, "w")
            elif keyboard.read_key() == "a":
                press(ser, "a")
            elif keyboard.read_key() == "s":
                press(ser, "s")
            elif keyboard.read_key() == "d":
                press(ser, "d")
            elif keyboard.read_key() == "j":
                press(ser, "A")
            elif keyboard.read_key() == "k":
                press(ser, "B")
            else:
                ser.write(b'0')
                time.sleep(.075)


if __name__ == '__main__':
    main()
