#! /usr/bin/env python
import pygame, sys
from pygame.locals import *

pygame.init()

pygame.display.set_caption('Arcade')

WHITE = (255, 255, 255); BLACK = (0, 0, 0)
BLUE = (0, 0, 255); RED = (255, 0, 0)
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 200
ZONE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FONT = pygame.font.SysFont('KacstOffice.ttf', 16)

ballRadius  = 10
ballX = 10
ballY = 10
ballModX = ballModY = 1

rectWidth = 320
rectHeight = 20
rectX = 0
rectY = SCREEN_HEIGHT - 2*rectHeight
modX = modY = 0

SOUND = pygame.mixer.Sound('arcade-jump-coin.wav')

clock = pygame.time.Clock()
while True:

    # game loop
    ZONE.fill(BLUE)

    RECT_COORDINATES = str('x:'+str(rectX)+' y:'+str(rectY))
    BALL_COORDINATES = str('x:'+str(ballX)+' y:'+str(ballY))
    print(ballX, ballY)
    BALL_SPEED = str(ballModY)
    TEXT = FONT.render(RECT_COORDINATES, True,WHITE)
    ZONE.blit(TEXT, (0,0))
    TEXT = FONT.render(BALL_COORDINATES, True,WHITE)
    ZONE.blit(TEXT, (550,0))
    TEXT = FONT.render(BALL_SPEED, True,WHITE)
    ZONE.blit(TEXT, (250,0))

    pygame.draw.rect(ZONE, WHITE, (rectX, rectY, rectWidth, rectHeight))
    pygame.draw.circle(ZONE, WHITE, ( ballX , ballY ), ballRadius)

    ballX += ballModX
    ballY += ballModY

    if ballX >= SCREEN_WIDTH - ballRadius or ballX <= 0 + ballRadius:
        SOUND.play()
        ballModX *= -1
    if ballY >= SCREEN_HEIGHT - ballRadius or ballY <= 0 + ballRadius:
        SOUND.play()
        ballModY *= -1

    if (ballX >= rectX) and (ballX <= rectX + rectWidth) and ((ballY + ballRadius) == rectY):
        ballModY *= -1
        SOUND.play()



    rectX += modX
    rectY += modY



    if rectX <= 0 or rectX >= SCREEN_WIDTH - rectWidth:
        modX = 0
    if rectY <= 0 or rectY >= SCREEN_HEIGHT - rectHeight:
        modY = 0

    # event capture statements
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()



        if keys[ pygame.K_RIGHT ]:

            if rectX >= 1230:
                modX = 0
            else:
                modX = 2
        elif keys[ pygame.K_LEFT ]:
            if rectX <= 0:
                modX = 0
            else:
                modX = -2
        elif keys[ pygame.K_UP ]:
            if rectY <= 0:
                modY = 0
            else:
                modY = -2
        elif keys[ pygame.K_DOWN ]:
            if rectY >= 780:
                modY = 0
            else:
                modY = 2
        else: modX = modY = 0




    clock.tick( 150 )


    pygame.display.update()
# Write your code here :-)
