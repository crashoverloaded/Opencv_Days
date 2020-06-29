import cv2

# Haar cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('faces.jpg')
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray , 1.1 , 4)

for (x,y,w,h) in faces:
	cv2.rectangle(img  , (x,y) , (x+w , y+h) , (0,255,0) , 3)

cv2.imshow('img' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()
