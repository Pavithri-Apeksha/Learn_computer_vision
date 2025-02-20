import cv2
source = cv2.VideoCapture(0)
while True:
    ret,img = source.read()
    if(ret==False):
        break
    imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    ret,thresh = cv2.threshold(imgGray,80,255,cv2.THRESH_BINARY)
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if(area>14000 and area<16000):
            cv2.drawContours(img,[cnt],-1,(0,0,255),2)
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow('thresh',thresh)
    cv2.imshow('IMG',img)
    key = cv2.waitKey(10)
    if(key==27):
        break


cv2.destroyAllWindows()