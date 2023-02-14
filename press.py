from __future__ import annotations
import time

import serial


def press(ser: serial.Serial, s: str, duration: float = .05):
    ser.write(s.encode())
    time.sleep(duration)
    ser.write(b'0')
    time.sleep(.075)


def main():
    with serial.Serial('COM4') as ser:
        press(ser, 'A')


if __name__ == '__main__':
    main()
