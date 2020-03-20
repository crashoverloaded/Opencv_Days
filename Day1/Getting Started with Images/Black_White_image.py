#!/usr/bin/python3

import numpy as np
import cv2 

# Creating a Black Image
# 512,512 is size , 3 is color channel (RGB), uint8 is the datatype containing 0 to 255
# Remember "0" for Black
img = np.zeros((512,512,3),np.uint8)
cv2.imshow('Blackie',img)

# Now White image
# The np.ones will create a array of 512x512 with ones and than we have multiplied every element to 255 to convert it in white
# Remember "255" for White
img_white = 255 * np.ones((512,200,3),np.uint8)
cv2.imshow('Whiteie',img_white)
cv2.waitKey(0)
cv2.destroyAllWindows()
