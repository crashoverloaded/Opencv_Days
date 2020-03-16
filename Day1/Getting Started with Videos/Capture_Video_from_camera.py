#!/usr/bin/python3

import numpy as np
import cv2 

# Argument can be Video File or Device Index
# "0" is for primary camera , you can also pass "1" or so on for another camera
cap = cv2.VideoCapture(0)


if not cap.isOpened():
	#If it is True, OK. Otherwise open it using cap.open().
	print("Cannot Open Camera BC !!!")
	exit()
while True:
	# Capture Frame by Frame
	# cap.read() return True/False
	# If frame is read correctly, it will be True and returned in ret variable
	ret , frame = cap.read()
	if not ret:
		print("Can't Recieve Frame BC ! (Stream End ho gayi Kya BC ?) .. EXIT KR RHA HU BC !")
		break
	# Converting from BGR to Grayscale 
	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Display Resluting Gray Frame 
	cv2.imshow('VIDEO',gray_frame)

	# Displaying Colored Frame
	cv2.imshow('COLORED_VIDEO',frame)

	# if waitkey = 0 passes than it waits indefinitely until key is stroked else if 1 is passed , than it does not wait indefinitely.
	if cv2.waitKey(1)  == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
