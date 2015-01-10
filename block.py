import pygame

class Block(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, colour):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def get_coord(self):
        coord = [self.rect.x, self.rect.y]
        return coord

    def move_paddle(self, direction, speed, display_width, paddle_width):
        if direction == 1 and self.rect.x + paddle_width < display_width:
            self.rect.x = self.rect.x + (direction * speed)


        if direction == -1 and self.rect.x > 0:
            self.rect.x = self.rect.x + (direction * speed)