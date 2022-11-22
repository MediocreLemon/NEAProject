import pygame, sys, os, time
from pygame.locals import *
from settings import *
#from roomgeneration import *

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
display = pygame.Surface((DISPLAY_WIDTH,DISPLAY_HEIGHT))

pygame.display.set_caption('Gaming Time')


#player defs
playerSprite = pygame.image.load("assets/playerSprites/idle/idle_0.png")
playerLocation = [50,50]
playerRect = pygame.Rect(playerLocation[0], playerLocation[1], playerSprite.get_width(), playerSprite.get_height())


# #ground defs
# floorSprite = pygame.image.load("assets/mapSprites/groundSprite.png")

# #wall defs
# topWall = pygame.image.load("assets/mapSprites/topWall.png")
# bottomWall = pygame.image.load("assets/mapSprites/bottomWall.png")
# leftWall = pygame.image.load("assets/mapSprites/leftWall.png")
# rightWall = pygame.image.load("assets/mapSprites/rightWall.png")
# baseWall = pygame.image.load("assets/mapSprites/baseWall.png")
# backgroundSprite = pygame.image.load("assets/mapSprites/background.png")



# #game map
# gameMap = [[]]

# #animation def
# global animationFrames
# animationFrames = []


# def loadAnimation(path,frameDuration): # accepts the path of the images and how long they last
# 	global animationFrames
# 	animationName = path.split("/")[-1] # takes the end of the split path
# 	animationFrameData = []
# 	n=0
# 	for frame in frameDuration: 
# 		animationFrameID = animationName + "_" + str(n)
# 		imageLocation = path + "/" + animationFrameID + ".png"
# 		animationImage = pygame.image.load(imageLocation).convert()
# 		animationImage.set_colorkey(WHITE)
# 		#animationFrames[animationFrameID] == animationImage.copy()
# 		for i in range(frame):
# 			animationFrameData.append(animationFrameID)
# 		n += 1
# 	return animationFrameData

# #print(loadAnimation("assets/playerSprites/run",[7,7,7,7]))

# animationDictionary = {}

# animationDictionary["run"] = loadAnimation("assets/playerSprites/run",[7,7,7,7]) # 7 frames per frame of animation
# animationDictionary["idle"] = loadAnimation("assets/playerSprites/idle", [30,30]) # 30 frames per frame of animation


#basic movement
movingUp = False
movingDown = False
movingLeft = False
movingRight = False



#main loop
while True:
	display.fill(DARK_GREY)

	playerRect.x = playerLocation[0]
	playerRect.y = playerLocation[1]


	display.blit(playerSprite, playerLocation)

	if movingRight == True:
		playerLocation[0] += 5
	if movingLeft == True:
		playerLocation[0] -= 5
	if movingUp == True:
		playerLocation[1] -= 5
	if movingDown == True:
		playerLocation[1] += 5
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		if event.type == KEYDOWN:
			if event.key == K_d:
				movingRight = True
			if event.key == K_a:
				movingLeft = True
			if event.key == K_w:
				movingUp = True
			if event.key == K_s:
				movingDown = True

		if event.type == KEYUP:
			if event.key == K_d:
				movingRight = False
			if event.key == K_a:
				movingLeft = False
			if event.key == K_w:
				movingUp = False
			if event.key == K_s:
				movingDown = False


	surf = pygame.transform.scale(display, (SCREEN_WIDTH, SCREEN_HEIGHT))
	screen.blit(surf, (0,0))

	pygame.display.update()
	clock.tick(TARGET_FPS) #stay at 60 fps
