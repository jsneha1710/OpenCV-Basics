import cv2
import numpy as np
img=cv2.imread(r"C:\Users\Sneha\Pictures\Face.png")
imgresized=cv2.resize(img,(300,500))
imggray=cv2.cvtColor(imgresized,cv2.COLOR_BGR2GRAY)
faceCascade=cv2.CascadeClassifier(r"C:\Users\Sneha\Documents\haarcascade_frontalface_default.xml")

faces=faceCascade.detectMultiScale(imggray,1.1,4)

for(x,y,w,h) in faces:
    cv2.rectangle(imgresized,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("output",imgresized)
cv2.waitKey(0)