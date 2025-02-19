import cv2
video_source = cv2.VideoCapture('hello.mp4')
#video_source = cv2.VideoCapture(0)

width = 640
height = 480

while True:
    ret,img = video_source.read()
    img_resized = cv2.resize(img, (width, height))
    if(ret==False):
        break
    cv2.imshow('Img',img_resized)
    key = cv2.waitKey(1)
    if(key==27): #press - esc
        break
    if(key==112):#press - p
        cv2.imwrite('Img-cap.png',img_resized)
    print(key)
cv2.destroyAllWindows()
