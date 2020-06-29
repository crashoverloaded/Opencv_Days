import cv2

# Haar cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
#img = cv2.imread('faces.jpg')
#gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

while cap.isOpened():
	_ , frame = cap.read()
	gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray , 1.1 , 4)
	for (x,y,w,h) in faces:
		cv2.rectangle(frame  , (x,y) , (x+w , y+h) , (0,255,0) , 3)

	cv2.imshow('img' , frame)
	if cv2.waitKey(1) == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
