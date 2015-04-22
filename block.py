import pygame

class Block(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, lives):
        pygame.sprite.Sprite.__init__(self)

        self.starting_lives = lives
        self.lives = lives
        self.image = pygame.Surface([width, height])


        if self.lives == 3:
            self.image.fill((0, 255, 0))#green
        elif self.lives == 2:
            self.image.fill((255, 153, 0))#orange
        elif self.lives == 1:
            self.image.fill((255, 0, 0))#red

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def get_coord(self):
        coord = [self.rect.x, self.rect.y]
        return coord

    def remove_life(self):
        self.lives -= 1
        if self.lives == 2:
            self.image.fill((255, 153, 0))#orange
        elif self.lives == 1:
            self.image.fill((255, 0, 0))#red
        elif self.lives < 1:
            return "dead"

#class Paddle(Block):
 #   def __init__(self, colour):
  #      Block.__init__():


    def move_paddle(self, direction, speed, display_width, paddle_width):
        if direction == 1 and self.rect.x + paddle_width < display_width:
            self.rect.x = self.rect.x + (direction * speed)


        if direction == -1 and self.rect.x > 0:
            self.rect.x = self.rect.x + (direction * speed)