#!/usr/bin/python3

import cv2
import numpy as np
import  matplotlib.pyplot as plt

#img = cv2.imread('/root/Downloads/dog.jpg')
#img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
cap = cv2.VideoCapture(0)
while cap.isOpened():
	_ , img = cap.read()
# Define Kernel
# Formaula of kernel is :- (1/kernel_wid * kernel_hei)* identity matrix
	kernel = np.ones((5,5),np.float32)/25

# Destination image
# Homogeneous Filter
	dst = cv2.filter2D(img,-1,kernel)

# Low pass Filter - used for removing noise and blurring image
# High pass Filter - helps in finding edges in image
# Blur method # Averaging
	blur = cv2.blur(img,(5,5))

# Gaussian Filter - it is nothing but using different weight kernel in both x and y direction 
# so in the result , pixel located in middle have bigger weight and in corner is lower weight
# Designed for removing high frequency noise 
	gblur = cv2.GaussianBlur(img , (5,5), 0)

# Median Filter- replaces each pixel with the median of its neighbouring pixels.
# great when dealing with "SAlt and Pepper Noise"
	median = cv2.medianBlur(img,5)

# Bilateral Image - Edges remain sharper while image is blur
	bilateral = cv2.bilateralFilter(img,9,75,75)
#title = ['Image','2D CONVOLUTION',"BLUR",'GBLUR','Median','Bilateral']
	cv2.imshow('Image',img)
	cv2.imshow('HOMO',dst)
	cv2.imshow('blur',blur)
	cv2.imshow('gblur',gblur)
	cv2.imshow('Median',median)
	cv2.imshow('Bilateral', bilateral)
#image = [img,dst,blur,gblur,median,bilateral]
	if cv2.waitKey(1) == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
'''
for i in range(6):
	plt.subplot(3,3,i+1),plt.imshow(image[i],'gray')
	plt.title(title[i])	
	plt.xticks([]),plt.yticks([])	

plt.show() 


'''
