import numpy as np
import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
	print("sa")
	exit()
while True:
	_ , frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	_ , th1 = cv2.threshold(frame, 50,255,cv2.THRESH_BINARY)
	th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
	th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
	cv2.imshow("fra",frame)
	cv2.imshow("thre_bin",th1)
	cv2.imshow("adap_mean",th2)
	cv2.imshow("adap_gaus",th3)
	if cv2.waitKey(1) == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
