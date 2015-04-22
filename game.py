#! /usr/bin/env python3
import ball
import block
import pygame

import Input

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

font = pygame.font.SysFont("monospace", 15)


def create_ball(display_width, display_height, ball_size):
    new_ball = ball.Ball(display_width, display_height, ball_size)

    ball_list.add(new_ball)

def create_block(x, y, width, height, lives):
    new_block = block.Block(x, y, width, height, lives)

    block_list.add(new_block)

def create_block_series(display_width, block_height, edge_spacing, block_spacing, columns, rows):
    blocks_width = display_width - (edge_spacing * 2) - (block_spacing * (columns - 1))
    block_width = (blocks_width / columns)
    lives = 3
    for i in range(0, columns):
        for j in range(0, rows):
            create_block(edge_spacing + (i * block_width) + (i * block_spacing), edge_spacing + (block_height + block_spacing) * j, block_width, block_height, lives)
    return block_width


block_width = create_block_series(display_width, block_height, 10, 2, 10, 4)

create_ball(display_width, display_height, ball_size)

clock = pygame.time.Clock()

paddle = block.Block(display_width/2-paddle_width/2, display_height - paddle_height * 1.2, paddle_width, paddle_height, 2)
paddle_list.add(paddle)

# score = 0
# draw_score()
lose = False

while lose != True:

    paddle_direction = Input.checkKeyPresses(paddle_direction)

    for paddle in paddle_list:
        paddle.move_paddle(paddle_direction, paddle_speed, display_width, paddle_width)

    dictionary_of_collided_balls = pygame.sprite.groupcollide(ball_list, block_list, False, False);
    for ball, hit_blocks in dictionary_of_collided_balls.items():

        ball.check_collisions(hit_blocks[0], block_height, ball_size, block_width)# need to adapt this later so that we check collisions if more than one block is hit!!!

        for i in hit_blocks:
            if i.remove_life() == "dead":
                block_list.remove(i)

    dictionary_of_collided_paddles = pygame.sprite.groupcollide(ball_list, paddle_list, False, False);
    for ball, i in dictionary_of_collided_paddles.items():
        ball.check_collisions(i[0], block_height, ball_size, block_width)
        #score += 1
        #draw_score()

    ball_list.update(ball_size, ball_list)

    if ball_list.sprites() == []:
        lose = True
        #screen.fill(red)
        pygame.display.update()
        pygame.time.delay(2000)


    #block_list.check()

    ball_list.draw(screen)
    block_list.draw(screen)
    paddle_list.draw(screen)

    text = "hello"
    score_label = font.render(text, 1, red)
    screen.blit(score_label, (0, 0))

    clock.tick(50)

    pygame.display.flip()

    screen.fill(black)