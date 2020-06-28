import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/root/Downloads/dog.jpg' , 0)

# New Method , 2nd arg is channel index (0 for grayscale)
# 3rd arg is image mask , 4rth is histsize or bin count
hist = cv2.calcHist([img] , [0] , None ,  [256] , [0,256])
plt.plot(hist)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()



