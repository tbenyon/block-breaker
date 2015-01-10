import pygame

white = (255, 255, 255)
black = (0, 0, 0)

class Ball(pygame.sprite.Sprite):

    def __init__(self, display_width, display_height, ball_size):
        pygame.sprite.Sprite.__init__(self)

        self.ball_speed = 6

        self.x_dir = self.ball_speed
        self.y_dir = -self.ball_speed

        self.display_width = display_width
        self.display_height = display_height

        self.image = pygame.image.load('apple.png').convert()

        self.image.set_colorkey(black)

        self.rect = self.image.get_rect()

        self.rect.x = (display_width / 2) - (ball_size / 2)
        self.rect.y = display_height - ball_size

    def update(self, ball_size, ball_list):

        self.rect.x += self.x_dir

        self.rect.y += self.y_dir

        if self.rect.x + ball_size > self.display_width or self.rect.x < 0:
            self.x_dir *= -1

        if self.rect.y < 0:
            self.y_dir *= -1

        if self.rect.y > self.display_height:
            ball_list.remove(self)

    def check_collisions(self, the_block, block_height, ball_size, block_width):
        block_x, block_y = the_block.get_coord()

        # below is used in case the ball moves a little way over into the shape
        allowance = self.ball_speed * 1.1

        #check bottom of block
        if self.y_dir < 0:
            if block_y + block_height >= self.rect.y and block_y + block_height - allowance <= self.rect.y:
                self.y_dir = self.y_dir * -1

        # check top of block
        if self.y_dir > 0:
            if self.rect.y + ball_size >= block_y and self.rect.y + ball_size <= block_y + allowance:
                self.y_dir = self.y_dir * -1

            #check left of block
        if self.x_dir > 0:
           if self.rect.x + ball_size >= block_x and self.rect.x + ball_size <= block_x + allowance:
                self.x_dir = self.x_dir * -1

            #check right of block
        if self.x_dir < 0:
           if self.rect.x <= block_x + block_width and self.rect.x >= block_x + block_width - allowance:
                self.x_dir = self.x_dir * -1