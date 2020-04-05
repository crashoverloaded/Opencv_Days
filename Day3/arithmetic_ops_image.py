import cv2

img = cv2.imread('/root/Downloads/Pic.jpg')

print(img.shape)
print(img.size)
print(img.dtype)

# Splitting into three channels
b,g,r = cv2.split(img)

# Merging bgr channels into image
img = cv2.merge((b,g,r))


cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()

