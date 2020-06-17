import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT

import snake_game

clock = pygame.time.Clock()
BOARD_SIZE = 20
BLOCK_SIZE = 30
SPEED = 100

palette = pygame.color.THECOLORS

SNAKE_COLOR = palette['black']
FOOD_COLOR = palette['red']
BOARD_COLOR = palette['white']

game_obj = snake_game.Game(BOARD_SIZE)

pygame.init()
window = pygame.display.set_mode((BOARD_SIZE * BLOCK_SIZE, BOARD_SIZE * BLOCK_SIZE))

pygame.display.set_caption("snake")


def render(game):
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            if (x, y) in game.snake:
                pygame.draw.rect(window, SNAKE_COLOR, rect)
            elif (x, y) == game.food:
                pygame.draw.rect(window, FOOD_COLOR, rect)
            else:
                pygame.draw.rect(window, BOARD_COLOR, rect)


move_event = pygame.USEREVENT + 1
pygame.time.set_timer(move_event, SPEED)

while not game_obj.game_over():
    

    for e in pygame.event.get():
        if e.type == move_event:
            game_obj.step()
        elif e.type == QUIT:
            sys.exit(0)
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                game_obj.change_dir("up")
            elif e.key == K_DOWN:
                game_obj.change_dir("down")
            elif e.key == K_LEFT:
                game_obj.change_dir("left")
            elif e.key == K_RIGHT:
                game_obj.change_dir("right")
    render(game_obj)
    pygame.display.update()
    clock.tick(30)
    
