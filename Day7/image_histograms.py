import numpy as np
import cv2
from matplotlib import pyplot as plt

#img = np.zeros((200,200) ,np.uint8)

#img = np.random.random_integers(0,255 , (200,200))
#cv2.rectangle(img , (0,100),(200,200), (255) , -1)
#cv2.rectangle(img , (0,50),(100,100), (127) , -1)
img = cv2.imread('/root/Downloads/dog.jpg')

# Splitting Image
b , g,r = cv2.split(img)
cv2.imshow("Image" , img)
cv2.imshow("B" , b)
cv2.imshow("G" , g)
cv2.imshow("R" , r)

plt.hist(img.ravel() ,256 , [0,256])
plt.hist(b.ravel() ,256 , [0,256])
plt.hist(g.ravel() ,256 , [0,256])
plt.hist(r.ravel() ,256 , [0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()



