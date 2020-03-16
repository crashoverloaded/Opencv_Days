#!/usr/bin/python3

import numpy as np
import cv2

# Load an color image in Grayscale
img = cv2.imread('/root/Downloads/canvas.png',0)

# Display image
cv2.imshow('Meme',img)

# Why 0xFF? 
'''
The 0xFF in this scenario is representing binary 11111111 a 8 bit binary, since we only require 8 bits to represent a character we AND waitKey(0) to 0xFF. As a result, an integer is obtained below 255.

ord(char) returns the ASCII value of the character which would be again maximum 255.

Hence by comparing the integer to the ord(char) value, we can check for a key pressed event and break the loop.
'''
# Hence we use it !
k = cv2.waitKey(0) & 0xFF 	

# If you Press "q" than it will quit
if k == ord('q'):
	cv2.destroyAllWindows()
# Else if you Press "s" than it'll save image and exit
elif k == ord('s'):
	cv2.imwrite('MEMEME.jpg',img)
	cv2.destroyAllWindows()

