import pygame
import Input


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        green = (0, 255, 0)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = 0
        self.speed = 10
        self.paddle_colour = green

        self.image = pygame.Surface([width, height])

        self.image.fill(green)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def get_coord(self):
        coord = [self.rect.x, self.rect.y]
        return coord

    def move_paddle(self, screen_width):

        self.direction = Input.checkKeyPresses(self.direction)

        if self.direction == 1 and self.rect.x + self.width < screen_width:
            self.rect.x += (self.direction * self.speed)


        if self.direction == -1 and self.rect.x > 0:
            self.rect.x += (self.direction * self.speed)