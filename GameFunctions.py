import pygame


def write(surface, words, size, color, background, location):
    font = pygame.font.Font(None, size)
    img = font.render(words, True, color, background)
    surface.blit(img, location)
