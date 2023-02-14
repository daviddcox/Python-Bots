from inputs import get_gamepad
import pygame
import threading


pygame.init()
position = [100, 100]
win = pygame.display.set_mode((800, 500))
run = True
value_x = 0
value_y = 0


def get_events():
    for thing in get_gamepad():
        events.append(thing)


while run:
    events = []
    thread1 = threading.Thread(target=get_events)
    thread1.start()
    win.fill((0, 0, 0))
    for event in events:
        print(event.code, event.state)
        if event.code == "ABS_X":
            value_x = event.state/100000
        if event.code == "ABS_Y":
            value_y = event.state / 100000
        if event.code == "BTN_SELECT":
            run = False

    position[0] += value_x
    position[1] -= value_y

    pygame.draw.circle(win, (255, 255, 255), (position[0], position[1]), 10)
    pygame.display.update()
