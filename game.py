import pgzrun
from random import randint
import os

WIDTH = 700
HEIGHT = 600

os.environ["SDL_VIDEO_CENTERED"]="1"
trackLeft=[]
trackRight=[]
trackCount=0
trackPosition = 350
trackWidth=150
trackDirection = False
SPEED = 4
gameStatus=0
gameStarted=False
car=Actor("racecar")
car.pos=350,560

def makeTrack():
	global trackLeft,trackRight,trackCount,trackPosition,trackWidth
	trackLeft.append(Actor("bare",pos=(trackPosition - trackWidth,0)))
	trackRight.append(Actor("bare",pos=(trackPosition + trackWidth,0)))
	trackCount+=1
def updateTrack():
	global trackLeft,trackRight,trackCount,trackPosition,trackWidth,trackDirection,SPEED,gameStatus
	b=0
	while b<len(trackLeft):
		if car.colliderect(trackLeft[b]) or car.colliderect(trackRight[b]):
			gameStatus=1
		trackLeft[b].y += SPEED
		trackRight[b].y += SPEED
		b += 1
	if trackLeft[len(trackLeft)-1].y>32:
		if trackDirection == False: trackPosition +=16
		if trackDirection == True: trackPosition -=16
		if randint(0,4) == 1: trackDirection = not trackDirection
		if trackPosition>700 -trackWidth:
			trackDirection=True
		if trackPosition<trackWidth:
			trackDirection=False
		makeTrack()
def draw():
	global gameStatus, trackCount, gameStarted
	screen.fill((128,128,128))
	if gameStatus==0:
		car.draw()
		b=0
		while b<len(trackLeft):
			trackLeft[b].draw()
			trackRight[b].draw()
			b +=1
		screen.draw.text("Your Current Score:"+str(trackCount),(10,10),color=(255,255,255))
	if gameStatus==1:
		screen.blit("redflag",(230,230))
		screen.draw.text("To win You Should Reach 500!",(100,60),color=(255,255,255),fontsize=50)
		screen.draw.text("Your Current Score:"+str(trackCount),(10,10),color=(255,128,0),fontsize=40)
	if gameStatus==2:
		screen.blit("finishflag",(230,230))
		screen.draw.text("You Won",(100,60),color=(255,255,255),fontsize=50)
def update():
	global gameStatus, trackCount, SPEED, trackWidth
	if gameStatus == 0:
		if keyboard.left:
			car.x -=2
		if keyboard.right:
			car.x +=2
		if keyboard.up:
			car.y -=2
		if keyboard.down:
			car.y +=2
		updateTrack()
	if trackCount>50: SPEED=5
	if trackCount>150: SPEED=6
	if trackCount>500: gameStatus=2
makeTrack()
pgzrun.go()