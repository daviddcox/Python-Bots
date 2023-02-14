import pygame
import colors
from classes import Button


pygame.init()


def write(text, font_size, color, bck_color, location):
    font = pygame.font.Font(None, font_size)
    img = font.render(text, True, color, bck_color)

    if location[0] == 'center':
        text_width = font.size(text)[0]
        location = (500 / 2 - text_width / 2, location[1])
    win.blit(img, location)


buttons = []

background = colors.white
win = pygame.display.set_mode((500, 500))
button1 = Button(30, win, colors.green, buttons, '1 Player', background, ('center', 300))
button2 = Button(30, win, colors.green, buttons, "2 Player", background, ('center', 350))
run = True
active = False
two_player = False
one_player = False
ev = pygame.event.get()
pos = (0, 0)
mouse = (0, 0, 0)
word = ''
letters = []
lives = 5


def main():
    pygame.time.delay(10)
    global ev
    ev = pygame.event.get()
    for events in ev:
        if events.type == pygame.QUIT:
            button1.active = False
            global run
            run = False
            button2.active = False

    global mouse
    mouse = pygame.mouse.get_pressed(3)
    global pos
    pos = pygame.mouse.get_pos()


def break_word(text):
    return [char for char in text]


while run:
    main()
    win.fill(background)
    write("Hangman", 40, colors.green, background, ('center', 50))

    for item in buttons:
        item.make_button()

    for event in ev:
        if event.type == pygame.MOUSEBUTTONDOWN:
            for item in buttons:
                if item.click(pos):
                    item.active = True
                    run = False

    pygame.display.update()

while button2.active:
    main()
    win.fill(background)
    while not active:
        write("Player 1 enter your word", 30, colors.green, background, ("center", 50))
        pygame.display.update()
        word = input('What is your word?')
        letters = break_word(word)
        print(letters)
        active = True
    y = 1
    x = 250 - 20*len(letters)/2
    win.fill(background)
    for i in letters:
        if i == " ":
            x += 20
        else:
            write("-", 30, colors.green, background, (x, 300))
            x += 20
    start_game = True
    pygame.display.update()
    while start_game:
        main()
        x = 250 - 20 * len(letters) / 2
        guess = input("Player 2 guess a letter")
        for letter in letters:
            if letter == guess:
                x = 250 - 20 * len(letters) / 2
                write(guess, 30, colors.black, background, (letters.index(letter)*20 + x, 250))
            else:
                pass
        pygame.display.update()


while button1.active:
    main()
    pygame.display.update()
