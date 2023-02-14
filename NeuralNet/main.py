import cv2
import mediapipe as mp
import pyautogui as pt

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cx = 100
cy = 100
cx1 = 100
cy1 = 100
tx = 200
ty = 200
px = 200
py = 200


while True:
    success, img = cap.read()
    imgRBG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRBG)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                if id == 8:
                    cx = int(1920 * (1 - lm.x))
                    cy = int(1080 * lm.y)
                    cx1, cy1 = int(lm.x * w), int(lm.y * h)
                if id == 4:
                    tx, ty = int(lm.x * w), int(lm.y * h)
                if id == 20:
                    px, py = int(lm.x * w), int(lm.y * h)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow('Image', img)
    cv2.waitKey(1)
    pt.moveTo(cx, cy)
    if abs(cx1 - tx) < 40 and abs(cy1 - ty) < 40:
        pt.mouseDown()
    else:
        pt.mouseUp()
    if abs(cx1 - px) < 40 and abs(cy1 - py) < 40:
        break
