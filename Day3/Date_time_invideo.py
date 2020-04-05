import cv2
import numpy as np
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
	ret , frame = cap.read()
	if not ret:
		print("Frame not extracted...")
		exit()
	# Font
	font = cv2.FONT_HERSHEY_SIMPLEX

	# Text to Print in video
	text = 'Width: '+str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + ' & Height :'+str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	cv2.putText(frame , text,(1,100),font,1 , (0,255,0),2,cv2.LINE_AA)

	# Datetime
	date = 'Date and Time:-' + str(datetime.datetime.now())	
	cv2.putText(frame , date,(1,60),font,1 , (0,255,255),2,cv2.LINE_AA)
	# ROI (Region of Interest)
	eyes = frame[200:300,200:300]
	frame[50:150,50:150] = eyes
	
	cv2.imshow('sa',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()

