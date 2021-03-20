# -*- coding: utf-8 -*-
import pygame
from sys import exit
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((300,200),0,32)
upImageFilename = 'game_start_up.png'
downImageFilename = 'game_start_down.png'

class Button(object):
    def __init__(self, upimage, downimage,position):
        self.imageUp = pygame.image.load(upimage).convert_alpha()
        self.imageDown = pygame.image.load(downimage).convert_alpha()
        self.position = position
        
    def isOver(self):
        point_x,point_y = pygame.mouse.get_pos()
        x, y = self. position
        w, h = self.imageUp.get_size()

        in_x = x - w/2 < point_x < x + w/2
        in_y = y - h/2 < point_y < y + h/2
        return in_x and in_y

    def render(self):
        w, h = self.imageUp.get_size()
        x, y = self.position
        
        if self.isOver():
            screen.blit(self.imageDown, (x-w/2,y-h/2))
        else:
            screen.blit(self.imageUp, (x-w/2, y-h/2))
    def is_start(self):
        b1,b2,b3 = pygame.mouse.get_pressed()
        if b1 == 1:
            return True

button = Button(upImageFilename,downImageFilename, (150,100))
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((200, 200, 200))
    button.render()
    if button.is_start():
        print ("start")
    pygame.display.update()
