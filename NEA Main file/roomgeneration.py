import pygame,os,sys,time
from settings import *
from main import *



#sprite definitions and numbers
background = pygame.image.load("assets/mapSprites/background.png")          #0
baseWall = pygame.image.load("assets/mapSprites/baseWall.png")              #1
bottomLeft = pygame.image.load("assets/mapSprites/bottomLeft.png")          #2
bottomRight = pygame.image.load("assets/mapSprites/bottomRight.png")        #3  
bottomWall = pygame.image.load("assets/mapSprites/bottomWall.png")          #4
darkWall = pygame.image.load("assets/mapSprites/darkWall.png")              #5
doorLocked = pygame.image.load("assets/mapSprites/doorLocked.png")          #6  
doorUnlocked = pygame.image.load("assets/mapSprites/doorUnlocked.png")      #7
groundSprite1 = pygame.image.load("assets/mapSprites/groundSprite1.png")    #8  
groundSprite2 = pygame.image.load("assets/mapSprites/groundSprite2.png")    #9
groundSprite3 = pygame.image.load("assets/mapSprites/groundSprite3.png")    #10
leftWall = pygame.image.load("assets/mapSprites/leftWall.png")              #11
rightWall = pygame.image.load("assets/mapSprites/rightWall.png")            #12
topLeft = pygame.image.load("assets/mapSprites/topLeft.png")                #13
topRight = pygame.image.load("assets/mapSprites/topRight.png")              #14
topWall = pygame.image.load("assets/mapSprites/topWall.png")                #15
torchWall = pygame.image.load("assets/mapSprites/torchWall.png")            #16

