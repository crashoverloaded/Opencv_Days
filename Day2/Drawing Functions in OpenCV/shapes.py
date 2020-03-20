#!/usr/bin/python3

import numpy as np
import cv2 

# Creating a Black Image
# 512,512 is size , 3 is color channel (RGB), uint8 is the datatype containing 0 to 255
# Remember "0" for Black
img = np.zeros((512,512,3),np.uint8)
cv2.line(img,(0,0),(512,512),(255,0,0),5)
cv2.imshow('Blackie',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
