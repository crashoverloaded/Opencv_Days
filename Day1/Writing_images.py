#!/usr/bin/python3

import numpy as np
import cv2

# Load an color image
img = cv2.imread('/root/Downloads/canvas.png')

# Loading colored image in grayscale 
img_gray = cv2.imread('/root/Downloads/canvas.png',0)

# Saving image

# First arg is Image name and second is image object
cv2.imwrite('New_Name.jpg',img)

# Saving gray image
cv2.imwrite('New_Gray_image.jpg',img_gray)

# By Above Operations , New images are Created named as "New_Name.jpg" and "New_Gray_image.jpg" in your current Folder
