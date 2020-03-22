#!/usr/bin/python3

import numpy as np
import cv2

img = cv2.imread('/root/Downloads/Pic.jpg')

# Matrix will be Printed
print(img)

# Printing value of bgr for 1st pixel 
print(img[0,0]) # will return [Blue,Green,Red]

# Changing value of Pixels from [0,1] to [9,10] to blue
for i in range(10):
	img[i,i+1] = [255,0,0]

# A line will be formed
cv2.imshow('sa',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
