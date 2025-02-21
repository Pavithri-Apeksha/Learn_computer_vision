import cv2
import numpy as np

img = cv2.imread('colors3.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_color = np.array((96,227,130))
upper_color = np.array((140,255,255))

mask = cv2.inRange(hsv,lower_color,upper_color)

cv2.imshow('IMG',img)
cv2.imshow('HSV',hsv)
cv2.imshow('mask',mask)



cv2.waitKey(0)
cv2.destroyAllWindows()

