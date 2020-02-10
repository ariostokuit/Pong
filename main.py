import pygame, sys
from pygame.locals import *
from pygame import math

pygame.init()

#Create window
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32))

#For the paddle and the ball
WHITE = (255, 255, 255, 255)





class Player:
    PLAYER_WIDTH = 10.0
    PLAYER_HEIGHT = 45.0
    PLAYER_SPEED = 15.0
    player_1 = Player(15.0, WINDOW_HEIGHT - Player.PLAYER_HEIGHT / 2)
    player_2 = Player((WINDOW_WIDTH - Player.PLAYER_WIDTH) - 15.0, Player.PLAYER_HEIGHT / 2)

    b1 = {'rect': pygame.Rect()}
    b2 = {'rect': pygame.Rect()}

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y




def main():
    while(True):
        for event in pygame.event.get():
            if event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()



if name == '__main__':
    main()