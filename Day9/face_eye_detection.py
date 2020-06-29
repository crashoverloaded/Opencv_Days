import cv2

# Haar cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
cap = cv2.VideoCapture(0)
#img = cv2.imread('faces.jpg')
#gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

while cap.isOpened():
	_ , frame = cap.read()
	gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray , 1.1 , 4)
	for (x,y,w,h) in faces:
		cv2.rectangle(frame  , (x,y) , (x+w , y+h) , (0,255,0) , 3)
		roi_gray = gray[y:y+h , x:x+w]
		roi_color = frame[y:y+h , x:x+w]	
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex ,ey , ew ,eh) in eyes:
			cv2.rectangle(roi_color  , (ex,ey) , (ex+ew , ey+eh) , (0,255,0) , 3)
		
	
	cv2.imshow('img' , frame)
	if cv2.waitKey(1) == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
