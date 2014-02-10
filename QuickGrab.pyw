"""
All coordinates assume a screen resolution of 1600x900
Chrome Browser right side of screen with bookmarks toolbar
5 down arrows
x_pad = 900
y_pad = 109
x_pad+1,y_pad+1,  x_pad+500,y_pad+700
"""

import ImageGrab
import os
import time

#Global Variables
x_pad = 900
y_pad = 109

def screenGrab():
	#upper left and lower right bounding box
	box = (x_pad+1,y_pad+1,  x_pad+500,y_pad+700)
	#Grab image from screen
	image = ImageGrab.grab(box)
	image.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
	
def main():
	screenGrab()

if __name__ == '__main__':
	main()
