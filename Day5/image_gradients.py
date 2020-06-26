#!/usr/bin/python3

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while cap.isOpened():
	_ , img = cap.read()
	gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

# LAPLACIAN 2nd argument is datatype 64 float , 3rd argument is kernel size  , it is optional
	lap = cv2.Laplacian(gray , cv2.CV_64F , ksize=5)

# Converting into Uint8
	lap = np.uint8(np.absolute(lap))
		
	cv2.imshow('laplacian', lap)
	cv2.imshow('Gray', gray)
#image = [img,dst,blur,gblur,median,bilateral]
	if cv2.waitKey(1) == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
