import cv2
import matplotlib.pyplot as plt
img = cv2.imread('gray_images.jpeg')
plt.imshow(img)
ret,img2 = cv2.threshold(img,80,255,cv2.THRESH_BINARY)
plt.imshow(img2,cmap='gray')
plt.show()
#cv2.imshow('IMG',img)
#cv2.waitKey(0)
#v2.destroyAllWindows()