#!/usr/bin/python3

import numpy as np
import cv2
import  matplotlib.pyplot as plt

img = cv2.imread('/root/Downloads/canvas.png',0)

# Using Matplotlib to plot or display image
plt.imshow(img,cmap='gray')

# to hide tick values on X and Y axis
plt.xticks([]), plt.yticks([])
plt.show()

## NOTE:-  OpenCV Load images in BGR Mode while Matplotlib displays in RGB Mode
