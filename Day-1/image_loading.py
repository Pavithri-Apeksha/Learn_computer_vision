import cv2
img = cv2.imread('sample-1.jpg')
print(img.shape)
img[:100,10]=[0,0,0]
# cv2.imshow('Flower',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
cv2.imwrite('New-sample.png',img)