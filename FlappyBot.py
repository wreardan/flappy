"""
All coordinates assume a screen resolution of 1600x900
Chrome Browser right side of screen with bookmarks toolbar
5 down arrows
x_pad = 900
y_pad = 109
x_pad+1,y_pad+1,  x_pad+500,y_pad+700
"""

import os
import time

import win32api, win32con

import ImageGrab
import ImageOps

from numpy import *

#Global Variables
x_pad = 900
y_pad = 109

def leftClick():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
	time.sleep(0.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
#	print 'Left Mouse Button Click'

def leftDown():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(.1)
	print 'Left Mouse Button Down'

def leftUp():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	time.sleep(.1)
	print 'Left Mouse Button Up'

def mousePos(coordinate):
	win32api.SetCursorPos((x_pad + coordinate[0], y_pad + coordinate[1]))

def moveLeftClick(coordinate):
	mousePos(coordinate)
	leftClick()
	time.sleep(0.1)
	print 'moveLeftClick' + str(coordinate)

def getCoordinates():
	x,y = win32api.GetCursorPos()
	x -= x_pad
	y -= y_pad
	print str(x) + ", " + str(y)

class Coordinate:
	menu_start = (149, 563)
	menu_click = (260, 298)
	menu_end = (149, 498)

	detect_loss = (256,369)

class Color:
	loss_pixel = (222,217,147)
	pipe_pixel = (64,57,52)

def startGame():
	#Start Menu
	moveLeftClick(Coordinate.menu_start)

	#Click to Start
	moveLeftClick(Coordinate.menu_click)

def endGame():
	#OK Button
	moveLeftClick(Coordinate.menu_end)
	

def screenGrab():
	#upper left and lower right bounding box
	box = (x_pad+1,y_pad+1,  x_pad+500,y_pad+700)
	#Grab image from screen
	image = ImageGrab.grab(box)
	#image.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
	return image

def playGame():
	moveLeftClick(Coordinate.menu_click)
	time.sleep(0.4)
	
	image = screenGrab()

	#scan horizontal line
	#convert line results
	#scan first pipe
	#scan second pipe
	#jumpTime = NeuralNetwork(secondPipeDistance, firstPipeHeight, secondPipeHeight)
	#time.sleep(jumpTime)
	#moveLeftClick(Coordinate.menu_click)

	#detect loss
	pixel = image.getpixel(Coordinate.detect_loss)
	if(pixel == Color.loss_pixel):
		print 'loss detected'
		return False
	return True
	
	
def main():
	while(True):
		startGame()
		while(playGame()):
			pass
		time.sleep(5)
		endGame()

if __name__ == '__main__':
	main()
