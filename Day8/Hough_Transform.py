import numpy as np
import cv2

img = cv2.imread('sudoku1.png',0)

# FINDING EDGES
edges = cv2.Canny(img , 50 ,150 ,apertureSize=3)
cv2.imshow('edge' , edges)
# Lines
# 2nd arg is rho(distance resolution in Pixels) , 3rd is theta(angle resolutions in radiance) , 4rth is threshold
lines = cv2.HoughLines(edges , 1 , np.pi /180 , 200)
for line in lines:
	rho , theta = line[0]
	a = np.cos(theta)
	b = np.sin(theta)
	
	x0 = a * rho
	y0 = b* rho
	
	# X1 -> r * cos(theta) - 1000 * sin(theata)
	x1 = int(x0 + 1000 * (-b))
	 
	# X1 -> r * sin(theta) + 1000 * cos(theata)
	y1 = int(y0 + 1000 * (a))
	# X1 -> r * cos(theta) + 1000 * sin(theata)
	x2 = int(x0 - 1000 * (-b))
	# X1 -> r * sin(theta) - 1000 * cos(theata)
	y2 = int(y0 - 1000 * (a))
	cv2.line(img , (x1,y1) , (x2,y2) , (0,0,255) , 2)

cv2.imshow('Image' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()
