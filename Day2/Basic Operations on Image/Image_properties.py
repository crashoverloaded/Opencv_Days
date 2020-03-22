#!/usr/bin/python3

import cv2
import numpy as np

img  = cv2.imread('/root/Downloads/Pic.jpg')

# It returns a tuple of number of rows, columns, and channels (if image is color)
# If an image is grayscale, the tuple returned contains only the number of rows and columns, so it is a good method to check whether the loaded image is grayscale or color.
print(img.shape)

# Total No of Pixels
print(img.size)

# Image Datatype
print(img.dtype)
