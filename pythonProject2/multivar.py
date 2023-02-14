import math

while True:
    x = int(input('x'))
    if x == 201:
        break
    y = int(input('y'))
    direction = input("min or max")

    run = True

    while run:
        "derivatives of z with respect to x and y"
        dx = -1*math.sin(x)
        dy = math.cos(y)

        "equation"
        z = math.cos(x) + math.sin(y)
        if -.001 < dx < .001 and -.001 < dy < .001:
            print("(", x, ",", y, ",", z, ")")
            run = False
        else:
            if direction == "min":
                x -= .25 * dx
                y -= .25 * dy
            elif direction == "max":
                x += .25 * dx
                y += .25 * dy
