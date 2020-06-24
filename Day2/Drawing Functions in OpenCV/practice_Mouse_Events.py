import cv2
import numpy as np
import datetime
img = np.zeros([512,512,3],np.uint8)
img = cv2.line(img , (0,0) , (212,212) , (0,0,255) , 4)

img = cv2.arrowedLine(img , (217,217) , (512,512) , (0,255,0) , 4)
img = cv2.rectangle(img , (150,150) , (300,300) , (255,0,0) , 4)
img = cv2.circle(img , (225,225) , 80 , (100,121,22), 4)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img , 'HELLO' , (50 , 100) , font , 4 , (255,255,255) , 4)
cv2.imshow('Blackie',img)
if cv2.waitKey(0) == ord('q'):
	cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)

img = cv2.line(img , (0,0) , (512,512) , (0,0,255) , 4)

while cap.isOpened():
	_ ,frame = cap.read()
	font = cv2.FONT_HERSHEY_SIMPLEX
	text1 = 'Width: '+ str(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	text2 = 'Height: '+str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	time = str(datetime.datetime.now())
	#cv2.putText(frame ,text1 , (300,100), font , 2 , (0,255,0) ,1 ,cv2.LINE_AA)
	#cv2.putText(frame , text2 , (300,150) , font , 2, (0,0,255) , 1, cv2.LINE_AA)
	cv2.putText(frame , time , (2,50) , font , 1, (0,0,255) , 1, cv2.LINE_AA)
	cv2.imshow('sa',frame)
	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()








# MOUSE EVENTS

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)
def click_event(event, x,y, flags, param):
	'''
	if event == cv2.EVENT_LBUTTONDOWN:
		cv2.circle(img , (x,y) , 5 , (0,0,255) , -1)
		points.append((x,y))
		if len(points) >= 2:
			cv2.line(img , points[-1] , points[-2], (255,0,0) ,4)
		cv2.imshow('frame', img)
	'''
	if event == cv2.EVENT_LBUTTONDOWN:
		blue = img[y,x,0]
		green = img[y,x,1]
		red = img[y,x,2]
		cv2.circle(img , (x,y), 3,(0,0,255),-1)
		im=np.zeros((512,512,3) ,np.uint8)
		im[:] = [blue , green , red]
		cv2.imshow('frame', img)			
		cv2.imshow('sa',im)

	if event == cv2.EVENT_RBUTTONDOWN:
		blue = img[y,x,0]
		green = img[y,x,1]
		red = img[y,x,2]
		print(blue , ', ', green,', ',red)
		font = cv2.FONT_HERSHEY_SIMPLEX 
		bgr = str(blue) + ', '+str(green) + ', '+str(red)
		cv2.putText(img , bgr , (x,y) , font , .5 , (0,255,255) , 2)
		cv2.imshow('frame', img)
		
img = cv2.imread('/root/Downloads/dog.jpg')
#img = np.zeros((512,512,3), np.uint8)
cv2.imshow('frame',img)
points = []
cv2.setMouseCallback('frame',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

