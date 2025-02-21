import cv2
import matplotlib.pyplot as plt
img = cv2.imread('Unequalized.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow('Gray Image',imgGray)
print(imgGray.shape)

flatten = imgGray.flatten()
print(flatten.shape)
plt.hist(flatten,bins=100)
plt.xlabel('Pixel value')
plt.ylabel('occurrence')
plt.show()

eqlImg = cv2.equalizeHist(imgGray)
cv2.imshow('eql',eqlImg)
plt.hist(eqlImg.flatten(),bins=100)
plt.xlabel('Pixel value')
plt.ylabel('occurrence')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()