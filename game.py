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

#recyclable sprite
class Recyclable(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image=pygame.image.load(img)
        self.image=pygame.transform.scale(self.image, (30, 30))
        self.rect=self.image.get_rect()

#non-recyclable sprite
class Non_recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("plastic.png")
        self.image=pygame.transform.scale(self.image, (40, 40))
        self.rect=self.image.get_rect()

images=["item1.png", "item2.png", "item3.png"]

#create sprite groups
item_group=pygame.sprite.Group()
plastic_group=pygame.sprite.Group()
all_sprites=pygame.sprite.Group()

#create item sprites
for i in range(50):
    item=Recyclable(random.choice(images))
    item.rect.x=random.randrange(WIDTH)
    item.rect.y=random.randrange(HEIGHT)
    item_group.add(item)
    all_sprites.add(item)

#create plastic sprites
for i in range(20):
    plastic=Non_recyclable()
    plastic.rect.x=random.randrange(WIDTH)
    plastic.rect.y=random.randrange(HEIGHT)
    plastic_group.add(plastic)
    all_sprites.add(plastic)

#create bin
bin=Bin()
all_sprites.add(bin)

#game variables
playing=True
score=0
clock=pygame.time.Clock()
start_time=time.time()
font=pygame.font.SysFont("Times New Roman", 22)
text=font.render(f"score: {score}", True, "red")

while playing:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
            pygame.quit()

    time_elapsed=time.time()-start_time

    if time_elapsed>=60:
        if score>=50:
            change_bg("winscreen.jpg")
        else:
            change_bg("losescreen.jpg")

    else:
        change_bg("bground.png")
        countdown=font.render(f"time left: {round(60-time_elapsed)}", True, "red")
        SCREEN.blit(countdown, (20, 10))
        
