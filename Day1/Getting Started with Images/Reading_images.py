#!/usr/bin/python3

import numpy as np
import cv2

# Load an color image
img = cv2.imread('/root/Downloads/canvas.png')

# Loading colored image in grayscale 
img_gray = cv2.imread('/root/Downloads/canvas.png',0)

# Display image

# First arg is Window name and second is image object
cv2.imshow('image',img)

# window for gray image
cv2.imshow('Gray_image',img_gray)

# Window waits for you to press any key for closing it.
cv2.waitKey(0)

# Destroying Windows after key press
cv2.destroyAllWindows()
