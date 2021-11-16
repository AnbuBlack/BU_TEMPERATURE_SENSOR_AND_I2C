import numpy as np 
import cv2
face_cascade = cv2.CascadeClassifier('C://opencv-4.x//data//haarcascades//haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(frame, (x,y),(x+w, y+h), (0,255,255), 2)

    cv2.imshow('faceTracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.release()    
cv2.destroyAllWindows()