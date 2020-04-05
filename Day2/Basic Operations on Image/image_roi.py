import cv2
import numpy as np
import matplotlib.pyplot as plt 

img = cv2.imread('/root/Downloads/piet.png')
#cv2.imshow('s',img)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.show()
