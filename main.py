import pygame, sys
from pygame.locals import *
from pygame import math

pygame.init()

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32))

WHITE = (255, 255, 255, 255)

class Player:
    PLAYER_WIDTH = 10.0
    PLAYER_HEIGHT = 45.0
    PLAYER_SPEED = 15.0
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

player_1 = Player(15.0, WINDOW_HEIGHT - Player.PLAYER_HEIGHT / 2)
player_2 = Player((WINDOW_WIDTH - Player.PLAYER_WIDTH) - 15.0, Player.PLAYER_HEIGHT / 2)

b1 = {'rect':pygame.Rect()}

def main():


if name == '__main__':
    main()