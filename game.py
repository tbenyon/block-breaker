#! /usr/bin/env python3
import sys
import ball
import block
import pygame
from pygame.locals import *



pygame.init()

display_width = 645
display_height = 300

screen = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Toms game')


ball_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
paddle_list = pygame.sprite.Group()

ball_size = 50


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (255, 0, 255)

block_height = 30

paddle_width = 100
paddle_height = 15
paddle_colour = green
paddle_direction = 0
paddle_speed = 10

#myfont = pygame.font.SysFont("monospace", 15)

def create_ball(display_width, display_height, ball_size):
    new_ball = ball.Ball(display_width, display_height, ball_size)

    ball_list.add(new_ball)

def create_block(x, y, width, height, colour):
    new_block = block.Block(x, y, width, height, colour)

    block_list.add(new_block)

def create_block_series(display_width, block_height, edge_spacing, block_spacing, columns, rows, colour):
    blocks_width = display_width - (edge_spacing * 2) - (block_spacing * (columns - 1))
    block_width = (blocks_width / columns)
    for i in range(0, columns):
        for j in range(0, rows):
            create_block(edge_spacing + (i * block_width) + (i * block_spacing), edge_spacing + (block_height + block_spacing) * j, block_width, block_height, colour)
    return block_width


# def draw_score():
#     label = myfont.render(score, 1, green)
#     screen.blit(label, (100, 100))


block_width = create_block_series(display_width, block_height, 10, 2, 5, 4, yellow)

create_ball(display_width, display_height, ball_size)

clock = pygame.time.Clock()

paddle = block.Block(display_width/2-paddle_width/2, display_height - paddle_height * 1.2, paddle_width, paddle_height, paddle_colour)
paddle_list.add(paddle)

# score = 0
# draw_score()
lose = False
while lose != True:

    for event in pygame.event.get():
        #print (event)  # This print just prints the activity (event in the window)
        if event.type == QUIT:
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

    for paddle in paddle_list:
        paddle.move_paddle(paddle_direction, paddle_speed, display_width, paddle_width)

    dictionary_of_collided_balls = pygame.sprite.groupcollide(ball_list, block_list, False, False);
    for ball, blocks in dictionary_of_collided_balls.items():

        ball.check_collisions(blocks[0], block_height, ball_size, block_width)# need to adapt this later so that we check collisions if more than one block is hit!!!

        block_list.remove(blocks[0])

    dictionary_of_collided_paddles = pygame.sprite.groupcollide(ball_list, paddle_list, False, False);
    for ball, i in dictionary_of_collided_paddles.items():
        ball.check_collisions(i[0], block_height, ball_size, block_width)
        #score += 1
        #draw_score()

    ball_list.update(ball_size, ball_list)

    if ball_list.sprites() == []:
        lose = True
        screen.fill(red)
        pygame.display.update()
        pygame.time.delay(2000)


    #block_list.check()

    ball_list.draw(screen)
    block_list.draw(screen)
    paddle_list.draw(screen)

    clock.tick(50)

    pygame.display.flip()

    pygame.display.update()

    screen.fill(black)
    
    
    
