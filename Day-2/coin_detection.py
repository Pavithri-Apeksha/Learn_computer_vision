import cv2
import matplotlib.pyplot as plt
img = cv2.imread('sl coins.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
plt.imshow(img,cmap='gray')

ret,img2 = cv2.threshold(imgGray,240,255,cv2.THRESH_BINARY)
plt.imshow(img2,cmap='gray')

contours , hierarchy = cv2.findContours(img2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#print(len(contours))
#print(contours[1])
#print(len(contours[3]))

#cv2.drawContours(img,contours,-1,(0,255,255),2)

for cnt in contours:
    area = cv2.contourArea(cnt)
    if(area>14000 and area<16000):
        #cv2.drawContours(img,[cnt],-1,(0,0,255),2)
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    print(area)


cv2.imshow('Thresh',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.show()