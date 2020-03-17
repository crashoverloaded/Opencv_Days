#!/usr/bin/python3

import numpy as np 
import cv2

cap = cv2.VideoCapture('/root/Downloads/bhai.mp4')

if not cap.isOpened():
	print("Kuch Gadbad Hai bc !")
	exit()
while True:
	ret , frame = cap.read()
	if not ret:
		print('Frame me Gadbad Hai !')
		break
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame_window',gray)
	if cv2.waitKey(1) == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
