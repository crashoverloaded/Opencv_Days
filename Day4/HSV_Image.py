#!/usr/bin/python3

import cv2
import numpy as np

def nothing(x):
	pass

# Buildin a Trackbar
# Name of Trackbar Window
cv2.namedWindow("Trackbar")

# Track for Lower Hue Value
# 1st Arg-> Name, 2-> Window , range->0,255 , pass function
cv2.createTrackbar("LH","Trackbar",0,255,nothing)

# Track for Lower Saturation Value
cv2.createTrackbar("LS","Trackbar",0,255,nothing)

# Track for Lower Value
cv2.createTrackbar("LV","Trackbar",0,255,nothing)

# Track for Upper Hue
cv2.createTrackbar("UH","Trackbar",255,255,nothing)

# Track for Upper Saturation
cv2.createTrackbar("US","Trackbar",255,255,nothing)

# Tracking for Upper value
cv2.createTrackbar("UV","Trackbar",255,255,nothing)

while True:
	
	frame = cv2.imread('/root/Downloads/maja.jpg')
	# Converting to HSV Image
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	# Getting Real Time Position From Trackbar of Different Values
	l_h = cv2.getTrackbarPos("LH","Trackbar")
	l_s = cv2.getTrackbarPos("LS","Trackbar")
	l_v = cv2.getTrackbarPos("LV","Trackbar")
	u_h = cv2.getTrackbarPos("UH","Trackbar")
	u_s = cv2.getTrackbarPos("US","Trackbar")
	u_v = cv2.getTrackbarPos("UV","Trackbar")
	
	# Changing HSV
	Lower = np.array([l_h,l_s,l_v])
	Upper = np.array([u_h,u_s,u_v])
	
	# Mask
	mask = cv2.inRange(hsv, Lower, Upper)
	res = cv2.bitwise_and(frame,frame,mask=mask)
	# Original
	cv2.imshow('frame',frame)
	# HSV
	cv2.imshow('hsv',hsv)
	# Final
	cv2.imshow('res',res)
	# Mask
	cv2.imshow('mask',mask)
	if cv2.waitKey(1) == ord('q'):
        	break

cv2.destroyAllWindows()

