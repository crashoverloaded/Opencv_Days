import cv2
import numpy as np

cap = cv2.VideoCapture(0)

_ , frame1 = cap.read()
_ , frame2 = cap.read()
while cap.isOpened():
	# FINDING Difference Between 1st and 2nd frame
	diff = cv2.absdiff(frame1 , frame2)
	gray = cv2. cvtColor(diff , cv2.COLOR_BGR2GRAY)

	# Blur
	blur = cv2.GaussianBlur(gray , (5,5) , 0)

	# Threshold
	_ , thresh = cv2.threshold(blur , 20 ,255 , cv2.THRESH_BINARY)

	# Dilation 
	dilate = cv2.dilate(thresh , None , iterations = 3)

	# COntours 
	contours , _ = cv2.findContours(dilate , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
	
	for contour in contours:
		(x,y,w,h) = cv2.boundingRect(contour)
		cv2.rectangle(frame1 , (x,y) , (x+w,y+h) , (0,255,0) , 3)
		cv2.putText(frame1 , "Status: {}".format('Movement'), (10,20) , cv2.FONT_HERSHEY_SIMPLEX , 1 , (0,255,0) , 3)
	#cv2.drawContours(frame1 , contours , -1 , (0,255,0) , 3)
	cv2.imshow('Frame' , frame1)
	frame1= frame2
	ret , frame2 = cap.read()
	if cv2.waitKey(1)  == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
