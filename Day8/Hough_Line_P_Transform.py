import numpy as np
import cv2

img = cv2.imread('sudoku.jpg',0)

# FINDING EDGES
edges = cv2.Canny(img , 50 ,150 ,apertureSize=3)
cv2.imshow('edge' , edges)
# Lines
# 2nd arg is rho(distance resolution in Pixels) , 3rd is theta(angle resolutions in radiance) , 4rth is threshold
lines = cv2.HoughLinesP(edges , 1 , np.pi /180 , 100 , minLineLength=100 , maxLineGap=10)
for line in lines:
	x1 , y1 ,x2 , y2 = line[0]
	cv2.line(img , (x1,y1) , (x2,y2) , (0,0,255) , 2)

cv2.imshow('Image' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()
