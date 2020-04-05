#!/usr/bin/python3

import numpy as np
import cv2 
import matplotlib.pyplot as plt
# Creating a Black Image
# 512,512 is size , 3 is color channel (RGB), uint8 is the datatype containing 0 to 255
# Remember "0" for Black
img = np.zeros((512,512,3),np.uint8)

#line
cv2.line(img,(0,0),(512,512),(255,0,0),5)

# Rectangle
cv2.rectangle(img,(30,30),(100,100),(0,0,255),9)

# Circle
cv2.circle(img,(40,10),23,(0,255,0),-1)

# Font
font = cv2.FONT_HERSHEY_SIMPLEX
# img , text , position , font , font size , color , thickness ,Line Type
cv2.putText(img,'HALLLE',(10,500),font,4,(0,255,0),2,cv2.LINE_AA)
cv2.imshow('Blackie',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
