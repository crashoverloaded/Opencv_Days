#!/usr/bin/python3

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
def nothing(x):
	pass
cv2.namedWindow("Trackbar")
cv2.createTrackbar("TH1" , "Trackbar" , 0 ,255 , nothing)
cv2.createTrackbar("TH2" , "Trackbar" , 0 ,255 , nothing)

while cap.isOpened():
	_ , img = cap.read()
	gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

	# Gaussian Pyramid 1/4th of original

	lower_resolution1 = cv2.pyrDown(gray)		

	# 1/4th of 1/4th 
 	
	lower_resolution2 = cv2.pyrDown(lower_resolution1)

	# Upper Resolution
	upper_resolution = cv2.pyrUp(lower_resolution2)


	cv2.imshow('Gray', gray)
	cv2.imshow('Gaussian_Down_lr1' , lower_resolution1)
	cv2.imshow('Gaussian_Down_lr2' , lower_resolution2)
	cv2.imshow('Gaussian_UP' , upper_resolution)
	if cv2.waitKey(1) == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
