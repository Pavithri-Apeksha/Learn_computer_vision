import cv2
img1 = cv2.imread('sample-rose.jpg')
img2=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

cv2.imshow('IMG1',img1)
cv2.imshow('IMG2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()