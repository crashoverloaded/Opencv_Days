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
	
	# CANNY 
	# 2nd and 3rd argument are threshold1 and threshold2
	#canny = cv2.Canny(gray , 100 ,200)
	# Creating Trackbar for threshold 1 and 2
	th1 = cv2.getTrackbarPos("TH1" , "Trackbar")
	th2 = cv2.getTrackbarPos("TH2" , "Trackbar")
	
	canny = cv2.Canny(gray , th1 ,th2)
	cv2.imshow('Canny', canny)
	if cv2.waitKey(1) == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
