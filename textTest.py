import pygame
from pygame.locals import *

pygame.init()

display_width = 645
display_height = 400
red = (255, 0, 0)
black = (0, 0, 0)
screen = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Toms game')

font = pygame.font.SysFont("monospace", 15)

while True:
    screen.fill(black)

    text = "hello"
    score_label = font.render(text, 1, red)
    screen.blit(score_label, (0, 0))


    pygame.display.flip()


