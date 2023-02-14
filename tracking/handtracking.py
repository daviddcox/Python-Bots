import mediapipe as mp
import cv2

import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True:
    success, img = cap.read()

    cv2.imshow("Image", img)
    cv2.waitKey(1)
