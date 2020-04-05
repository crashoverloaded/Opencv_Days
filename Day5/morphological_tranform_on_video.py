#!/usr/bin/python3

import cv2
import numpy as np
import  matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

while True:
	_ , mask = cap.read()

	# _, mask = cv2.threshold(img , 220 ,255 , cv2.THRESH_BINARY_INV)


	# kernel
	kernel = np.ones((3,3),np.uint8)
	# Dialation Method 
	dilation = cv2.dilate(mask,kernel,iterations = 2)

	# Erosion Method
	erosion = cv2.erode(mask, kernel , iterations = 2)

	# Opening Method
	# Opening is mix of Erosion and Dialtion 
	# first Erosion takes place than dilation
	opening = cv2.morphologyEx(mask , cv2.MORPH_OPEN , kernel)

	# Closing Method
	# Reverse of Open Method , Dialtion First , Erosion after
	closing = cv2.morphologyEx(mask , cv2.MORPH_CLOSE , kernel)
	cv2.imshow('mask',mask)
	#cv2.imshow('simple',img)
	cv2.imshow('dilation',dilation)
	cv2.imshow('erosion',erosion)
	cv2.imshow('opening',opening)
	cv2.imshow('closing',closing)
	if cv2.waitKey(1) == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()

