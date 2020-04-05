#!/usr/bin/python3

import cv2
import numpy as np
import  matplotlib.pyplot as plt

img = cv2.imread('/root/Downloads/bals.JPG', cv2.IMREAD_GRAYSCALE)

_, mask = cv2.threshold(img , 220 ,255 , cv2.THRESH_BINARY_INV)


# kernel
kernel = np.ones((5,5),np.uint8)
# Dialation Method 
dilation = cv2.dilate(mask,kernel,iterations = 2)

# Erosion Method
erosion = cv2.erode(mask, kernel , iterations = 1)

# Opening Method
# Opening is mix of Erosion and Dialtion 
# first Erosion takes place than dilation
opening = cv2.morphologyEx(mask , cv2.MORPH_OPEN , kernel)

# Closing Method
# Reverse of Open Method , Dialtion First , Erosion after
closing = cv2.morphologyEx(mask , cv2.MORPH_CLOSE , kernel)
title = ['Image','mask','dilation', 'Erosion', 'Opening', 'Closing']
image = [img,mask,dilation,erosion, opening,closing]

for i in range(6):
	plt.subplot(3,3,i+1),plt.imshow(image[i],'gray')
	plt.title(title[i])	
	plt.xticks([]),plt.yticks([])	

plt.show() 
