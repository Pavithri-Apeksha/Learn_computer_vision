import cv2
img1 = cv2.imread('sample-rose.jpg')
img2 = cv2.imread('sample-rose.jpg',0)
cv2.imshow('Img1',img1)
cv2.imshow('Img2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()