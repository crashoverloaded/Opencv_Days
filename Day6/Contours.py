#!/usr/bin/python3

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
def nothing(x):
	pass
cv2.namedWindow("Trackbar")
cv2.createTrackbar("LT" , "Trackbar" , 0 ,255 , nothing)
cv2.createTrackbar("UT" , "Trackbar" , 0 ,255 , nothing)

while cap.isOpened():
	_ , img = cap.read()
	gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
	
	# Creating Trackbar for threshold 1 and 2
	th1 = cv2.getTrackbarPos("LT" , "Trackbar")
	th2 = cv2.getTrackbarPos("UT" , "Trackbar")

	# Threshold	
	ret,thresh = cv2.threshold(gray ,th1 , th2 , 0)
	
	# Finding Contours , 2nd arg is Contour Mode or Contour retrieval mode , 3rd arg is Method
	contours , hierarchy = cv2.findContours(thresh , cv2.RETR_TREE , cv2.CHAIN_APPROX_NONE)
	print("No. of Contours:- "+str(len(contours)))
	
	# Draw Contours 3rd arg is index
	cv2.drawContours(img , contours , -1 , (0,255,0) , 3)
	cv2.imshow('image',img)
	if cv2.waitKey(1) == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
