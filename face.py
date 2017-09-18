import numpy as np
import cv2

#face_cascade = cv2.CascadeClassifier('C:\\code\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
#side_cascade = cv2.CascadeClassifier('C:\\code\\opencv\\build\\etc\\haarcascades\\haarcascade_profileface.xml')
#smile_cascade = cv2.CascadeClassifier('C:\\code\\opencv\\build\\etc\\haarcascades\\haarcascade_smile.xml')

face_cascade = cv2.CascadeClassifier('/usr/local/Cellar/opencv/3.3.0_2/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')
side_cascade = cv2.CascadeClassifier('/usr/local/Cellar/opencv/3.3.0_2/share/OpenCV/haarcascades/haarcascade_profileface.xml')
cat_cascade = cv2.CascadeClassifier('/usr/local/Cellar/opencv/3.3.0_2/share/OpenCV/haarcascades/haarcascade_frontalcatface.xml')


cap = cv2.VideoCapture(0)

while(True):
    ret, img = cap.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        side_faces = side_cascade.detectMultiScale(gray, 1.3, 5)
        cat_faces = cat_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

        for (x,y,w,h) in side_faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

        for (x,y,w,h) in cat_faces:
            cv2.rectangle(img,(x,y),(x+w,y+h), (0, 255, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]



        cv2.imshow('img', img)
    else:
        print('Can\'t capture')
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
