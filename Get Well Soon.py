from pygame import *
from pygame.locals import *
import pygame, pygame.locals, time, random, sys
ON = True

#MAIN------------------------------------------
pygame.init()
screen = pygame.display.set_caption("GET WELL SOON")
screen = pygame.display.set_mode((500,500))
pygame.display.update()
#----------------------------------------------

signw = pygame.image.load("signw.png").convert_alpha()
sign = pygame.image.load("sign.png").convert_alpha()
black = pygame.image.load("black.png").convert()
red = pygame.image.load("red.png").convert()
orange = pygame.image.load("orange.png").convert()
yellow = pygame.image.load("yellow.png").convert()
green = pygame.image.load("green.png").convert()
dgreen = pygame.image.load("dgreen.png").convert()
blue = pygame.image.load("blue.png").convert()
dblue = pygame.image.load("dblue.png").convert()
violet = pygame.image.load("violet.png").convert()
pink = pygame.image.load("pink.png").convert()
grey = pygame.image.load("grey.png").convert()

signw = pygame.transform.scale(signw, (500,500))
sign = pygame.transform.scale(sign, (500,500))
black = pygame.transform.scale(black, (500,500))
red = pygame.transform.scale(red, (500,500))
orange = pygame.transform.scale(orange, (400,400))
yellow = pygame.transform.scale(yellow, (300,300))
green = pygame.transform.scale(green, (200,200))
dgreen = pygame.transform.scale(dgreen, (100,100))
blue = pygame.transform.scale(blue, (500,500))
dblue = pygame.transform.scale(dblue, (150,150))
violet = pygame.transform.scale(violet, (100,100))
pink = pygame.transform.scale(pink, (50,50))
grey = pygame.transform.scale(grey, (40,40))

def original():
    screen.blit(red, (0,0))
    screen.blit(orange, (50,50))
    screen.blit(yellow, (100,100))
    screen.blit(green, (150,150))
    screen.blit(dgreen, (200,200))
    screen.blit(dblue, (350,350))
    screen.blit(violet, (350,350))
    screen.blit(pink, (350,350))
    screen.blit(dblue, (0,0))
    screen.blit(violet, (50,50))
    screen.blit(pink, (100,100))
    screen.blit(dblue, (350,0))
    screen.blit(violet, (350,50))
    screen.blit(pink, (350,100))
    screen.blit(dblue, (0,350))
    screen.blit(violet, (50,350))
    screen.blit(pink, (100,350))
    screen.blit(grey, (230,230))

original()

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit(0)
        exit()

while ON:
    count = 1
    signcount = 1
    while count <= 10 and signcount <= 10:
        time.sleep(0.5)
        if signcount % 2 == 0:
            screen.blit(sign, (0,0))
            pygame.display.update()
        elif signcount % 2 == 1:
            screen.blit(signw, (0,0))
            pygame.display.update()
        blue.set_alpha(20)
        screen.blit(blue, (0,0))
        pygame.display.update()
        signcount += 1
        count += 1
    while count <= 20 and count >= 11 and signcount <= 20 and signcount >= 11:
        time.sleep(0.5)
        if signcount % 2 == 0:
            screen.blit(sign, (0,0))
            pygame.display.update()
        elif signcount % 2 == 1:
            screen.blit(signw, (0,0))
            pygame.display.update()
        black.set_alpha(20)
        screen.blit(black, (0,0))
        pygame.display.update()
        count += 1
        signcount += 1
        if count >= 20:
            screen.fill((255,255,255))
            original()
