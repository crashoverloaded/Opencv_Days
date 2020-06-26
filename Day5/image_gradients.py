#!/usr/bin/python3

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while cap.isOpened():
	_ , img = cap.read()
	gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

# LAPLACIAN 2nd argument is datatype 64 float , 3rd argument is kernel size  , it is optional
	lap = cv2.Laplacian(gray , cv2.CV_64F , ksize=5)
	
# SobelX 2nd arg is datatype 64 float 3rd is value of dx and 4th is dy
	sobelX = cv2.Sobel(gray , cv2.CV_64F , 1 ,0)
	sobelX = np.uint8(np.absolute(sobelX))

# SObelY
	sobelY = cv2.Sobel(gray , cv2.CV_64F , 0 ,1)
	sobelY = np.uint8(np.absolute(sobelY))

# Sobel Combined
	sobel_com = cv2.bitwise_or(sobelX ,sobelY)
# Converting into Uint8
	lap = np.uint8(np.absolute(lap))
		
	cv2.imshow('laplacian', lap)
	cv2.imshow('SobelX', sobelX)
	cv2.imshow('Sobel_Y', sobelY)
	cv2.imshow('Sobel_Com', sobel_com)
	cv2.imshow('Gray', gray)
#image = [img,dst,blur,gblur,median,bilateral]
	if cv2.waitKey(1) == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
