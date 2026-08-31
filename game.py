import pygame
import random
from pygame.locals import *
import time

pygame.init()

pygame.display.set_caption("recycled management game!")
WIDTH=900
HEIGHT=700
SCREEN=pygame.display.set_mode((WIDTH, HEIGHT))

#function to change bg
def change_bg(img):
    bg=pygame.image.load(img)
    bg=pygame.transform.scale(bg, (WIDTH, HEIGHT))
    SCREEN.blit(bg, (0, 0))

#player sprite
class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("bin.png")
        self.image=pygame.transform.scale(self.image, (40, 60))
        self.rect=self.image.get_rect()
