import pygame


class Button:
    def __init__(self, font_size, win, color, buttons, text, background, location,):
        self.text_width = 0
        self.text_height = 0
        self.location = (0, 0)
        self.font_size = font_size
        self.win = win
        self.color = color
        buttons.append(self)
        self.active = False
        self.bck_color = background
        self.text = text
        self.location = location

    def make_button(self):
        font = pygame.font.Font(None, self.font_size)
        img = font.render(self.text, True, self.color, self.bck_color)
        self.text_width, self.text_height = font.size(self.text)
        if self.location[0] == 'center':
            self.location = (250 - self.text_width/2, self.location[1])
        self.win.blit(img, self.location)

    def click(self, mouse_pos):
        if (
            self.location[0] < mouse_pos[0] < self.location[0] + self.text_width
            and self.location[1] < mouse_pos[1] < self.location[1] + self.text_height
        ):
            return True
        else:
            return False
