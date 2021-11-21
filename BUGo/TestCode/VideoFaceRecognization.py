import numpy as np 
import cv2
face_cascade = cv2.CascadeClassifier('/home/pi/DataBase/first_module/opencv-4.x/data/haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    rotated = cv2.rotate(frame, cv2.ROTATE_180)
    gray = cv2.cvtColor(rotated,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(rotated, (x,y),(x+w, y+h), (0,255,255), 2)

    
    cv2.imshow('Face Tracking Rotated', rotated)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   
cv2.destroyAllWindows()