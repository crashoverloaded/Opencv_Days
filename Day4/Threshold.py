#!/usr/bin/python3

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
	# Reading Frame
	_ , frame = cap.read()
	
	# Threshold Binary in this , values less than 50 will be black else white
	_ , th1 = cv2.threshold(frame , 50 , 255 , cv2.THRESH_BINARY)
	
	# Threshold Binary INverse
	_ , th2 = cv2.threshold(frame,200,255,cv2.THRESH_BINARY_INV)
	
	# Threshold trunc , in this upto 120 the values remain unchanged
	_ , th3 = cv2.threshold(frame , 120 , 255, cv2.THRESH_TRUNC)

	# In this value will be 0 upto 120 after it will remain unchanged
	_ , th4 = cv2.threshold(frame , 120 , 255, cv2.THRESH_TOZERO)
	
	# INveerse of above one
	_ , th5 = cv2.threshold(frame , 120 , 255, cv2.THRESH_TOZERO_INV)

	cv2.imshow("fra",frame)
	cv2.imshow("threshold",th1)
	cv2.imshow("thre_inv",th2)
	cv2.imshow("thre_Trucn",th3)	
	cv2.imshow("zero",th4)
	cv2.imshow("zero_inv",th5)
	if cv2.waitKey(1) == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()

