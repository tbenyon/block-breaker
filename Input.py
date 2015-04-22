import sys
import pygame
from pygame.locals import *



def checkKeyPresses(paddle_direction):
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_direction = -1
            if event.key == pygame.K_RIGHT:
                paddle_direction = 1


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                paddle_direction = 0
            if event.key == pygame.K_RIGHT:
                paddle_direction = 0
    return paddle_direction