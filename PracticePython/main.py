# import pygame module in this program 
import pygame

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension..e(500, 500).
win = pygame.display.set_mode((800, 500))

pygame.display.set_caption("Coloring Game")

# marker current co-ordinates
x = 200
y = 200
x1 = 400
y1 = 200
x2 = 100
y2 = 200
x3 = 400
y3 = 400
# dimensions of the marker
width = 10
height = 10

# velocity / speed of movement
vel = 1
item = 0
colored = 0
circle1 = (0, 255, 0)
circle2 = (0, 0, 255)
colored2 = 0
colored3 = 0
circle3 = (255, 0, 0)
circle4 = (255, 0, 255)
colored4 = 0

# Indicates pygame is running
run = True

# infinite loop
while run:
    # creates time delay of 10ms
    pygame.time.delay(10)
    background = [(0, 0, 0), (255, 0, 0), (255, 137, 0), (255, 230, 0),
                  (37, 198, 32), (0, 102, 255), (154, 0, 255), (255, 0, 213)]
    color = [(255, 255, 255), (255, 0, 0), (255, 137, 0), (255, 230, 0),
             (37, 198, 32), (0, 102, 255), (154, 0, 255), (255, 0, 213)]
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # it will make exit the while loop
            run = False
    # stores keys pressed
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed(3)

    if mouse[0]:
        pos = pygame.mouse.get_pos()
        x3 = pos[0]
        y3 = pos[1]

    if mouse[1]:
        if colored4 <= 6:
            colored4 += 1
            circle4 = color[colored4]
            pygame.time.delay(300)

    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and x > 0:
        # decrement in x co-ordinate
        x -= vel

    # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and x < 800 - width:
        # increment in x co-ordinate
        x += vel

    # if left arrow key is pressed
    if keys[pygame.K_UP] and y > 0:
        # decrement in y co-ordinate
        y -= vel

    # if left arrow key is pressed
    if keys[pygame.K_DOWN] and y < 500 - height:
        # increment in y co-ordinate
        y += vel
    if keys[pygame.K_a] and x1 > 0:
        # decrement in x co-ordinate
        x1 -= vel

    # if left arrow key is pressed
    if keys[pygame.K_d] and x1 < 800 - width:
        # increment in x co-ordinate
        x1 += vel

    # if left arrow key is pressed
    if keys[pygame.K_w] and y1 > 0:
        # decrement in y co-ordinate
        y1 -= vel

    # if left arrow key is pressed
    if keys[pygame.K_s] and y1 < 500 - height:
        # increment in y co-ordinate
        y1 += vel
    if keys[pygame.K_o]:
        # increment in y co-ordinate
        if item <= 6:
            item += 1
            win.fill((background[item]))
            pygame.time.delay(500)
        else:
            item = 0
            win.fill((background[item]))
            pygame.time.delay(500)
    if keys[pygame.K_l]:
        if colored <= 6:
            colored += 1
            circle1 = color[colored]
            pygame.time.delay(300)
        else:
            colored = 0
            circle1 = color[colored]
            pygame.time.delay(300)
    if keys[pygame.K_q]:
        if colored2 <= 6:
            colored2 += 1
            circle2 = color[colored2]
            pygame.time.delay(300)
        else:
            colored2 = 0
            circle2 = color[colored2]
            pygame.time.delay(300)
    if keys[pygame.K_f] and x2 > 0:
        # decrement in x co-ordinate
        x2 -= vel

    # if left arrow key is pressed
    if keys[pygame.K_h] and x2 < 800 - width:
        # increment in x co-ordinate
        x2 += vel

    # if left arrow key is pressed
    if keys[pygame.K_t] and y2 > 0:
        # decrement in y co-ordinate
        y2 -= vel

    # if left arrow key is pressed
    if keys[pygame.K_g] and y2 < 500 - height:
        # increment in y co-ordinate
        y2 += vel
    if keys[pygame.K_y]:
        if colored3 <= 6:
            colored3 += 1
            circle3 = color[colored3]
            pygame.time.delay(300)
        else:
            colored3 = 0
            circle3 = color[colored3]
            pygame.time.delay(300)

    # drawing spot on screen which is rectangle here
    pygame.draw.circle(win, circle1, (x, y), height)
    pygame.draw.circle(win, circle2, (x1, y1), height)
    pygame.draw.circle(win, circle3, (x2, y2), height)
    pygame.draw.circle(win, circle4, (x3, y3), height)

    # it refreshes the window
    pygame.display.update()

# closes the pygame window
pygame.quit()
