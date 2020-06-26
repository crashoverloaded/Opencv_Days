import cv2
import numpy as np 
import time
def nothing(x):
        pass


cv2.namedWindow("Tracking1")
cv2.createTrackbar("LH","Tracking1",0,255,nothing)
cv2.createTrackbar("LS","Tracking1",0,255,nothing)
cv2.createTrackbar("LV","Tracking1",0,255,nothing)
cv2.createTrackbar("UH","Tracking1",255,255,nothing)
cv2.createTrackbar("US","Tracking1",255,255,nothing)
cv2.createTrackbar("UV","Tracking1",255,255,nothing)

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH","Tracking",0,255,nothing)
cv2.createTrackbar("LS","Tracking",0,255,nothing)
cv2.createTrackbar("LV","Tracking",0,255,nothing)
cv2.createTrackbar("UH","Tracking",255,255,nothing)
cv2.createTrackbar("US","Tracking",255,255,nothing)
cv2.createTrackbar("UV","Tracking",255,255,nothing)
cap = cv2.VideoCapture(0)

# We give some time for the camera to warm-up!
time.sleep(3)

background=0

for i in range(30):
	ret,background = cap.read()

# Laterally invert the image / flip the image.
background = np.flip(background,axis=1)

while True:
# Capturing the live frame
	ret, img = cap.read()

# Laterally invert the image / flip the image
	img  = np.flip(img,axis=1)

# converting from BGR to HSV color space
	hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	l_h = cv2.getTrackbarPos("LH","Tracking")
	l_s = cv2.getTrackbarPos("LS","Tracking")
	l_v = cv2.getTrackbarPos("LV","Tracking")
	u_h = cv2.getTrackbarPos("UH","Tracking")
	u_s = cv2.getTrackbarPos("US","Tracking")
	u_v = cv2.getTrackbarPos("UV","Tracking")
        # Blue
	lower_red = np.array([l_h,l_s,l_v])
	upper_red = np.array([u_h,u_s,u_v])
# Range for lower red
	#lower_red = np.array([0,120,70])
	#upper_red = np.array([10,255,255])
	mask1 = cv2.inRange(hsv, lower_red, upper_red)

# Range for upper range
	#lower_red = np.array([170,120,70])
	#upper_red = np.array([180,255,255])
	l_h = cv2.getTrackbarPos("LH","Tracking1")
	l_s = cv2.getTrackbarPos("LS","Tracking1")
	l_v = cv2.getTrackbarPos("LV","Tracking1")	
	u_h = cv2.getTrackbarPos("UH","Tracking1")
	u_s = cv2.getTrackbarPos("US","Tracking1")
	u_v = cv2.getTrackbarPos("UV","Tracking1")
	lower_red = np.array([l_h,l_s,l_v])
	upper_red = np.array([u_h,u_s,u_v])
	mask2 = cv2.inRange(hsv,lower_red,upper_red)

# Generating the final mask to detect red color
	mask = mask1+mask2

	mask1 = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
	mask1 = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3),np.uint8))


#creating an inverted mask to segment out the cloth from the frame
	mask2 = cv2.bitwise_not(mask1)


#Segmenting the cloth out of the frame using bitwise and with the inverted mask
	res1 = cv2.bitwise_and(img,img,mask=mask2)
	# creating image showing static background frame pixels only for the masked region
	res2 = cv2.bitwise_and(background, background, mask = mask1)


#Generating the final output
	final_output = cv2.addWeighted(res1,1,res2,1,0)
	cv2.imshow("magic",final_output)
	if cv2.waitKey(1) == ord('q'):
		break

	#cv2.imshow('ss',res1)
	#if cv2.waitKey(1) == ord('q'):
	#	break
cap.release()
cv2.destroyAllWindows()
