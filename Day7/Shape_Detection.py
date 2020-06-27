import numpy as np 
import cv2

img = cv2.imread('shapes.png')
img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
# Finding Threshold
_ , thresh = cv2.threshold(img , 240 , 255 , cv2.THRESH_BINARY)

# CONTOURS
contours , _ = cv2.findContours(thresh , cv2.RETR_TREE , cv2.CHAIN_APPROX_NONE)

# Iterating 
for i  in contours:
	# this method approximates polygonal curve
	# 2nd arg is epsilon , it is parameter specifying approximation accuracy , arcLength calc curve length , True is for closed shapes
	approx = cv2.approxPolyDP( i , 0.01 * cv2.arcLength(i , True), True)
	cv2.drawContours(img , [approx], 0 , (0,255,0) , 5)
	
	# Finding coordinates of shapes
	x = approx.ravel()[0]
	y = approx.ravel()[1]
	if len(approx) == 3:
		cv2.putText(img , "Triangle" , (x ,y) ,cv2.FONT_HERSHEY_COMPLEX , 0.5 , (0,0,255))
	elif len(approx) == 4:
		x , y  , w , h = cv2.boundingRect(approx)
		aspect_ratio = float(w) / float(h)
		print(aspect_ratio)
		if aspect_ratio >= 0.95 and aspect_ratio <= 1.05: 
			cv2.putText(img , "SQUARE" , (x ,y) ,cv2.FONT_HERSHEY_COMPLEX , 0.5 , (0,0,255))
		else:
			cv2.putText(img , "Rectangle" , (x ,y) ,cv2.FONT_HERSHEY_COMPLEX , 0.5 , (0,0,255))
	else:
		cv2.putText(img , "Circle" , (x ,y) ,cv2.FONT_HERSHEY_COMPLEX , 0.5 , (0,0,255))
cv2.imshow('Image' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()


