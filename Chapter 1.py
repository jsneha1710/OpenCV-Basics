import cv2
import numpy as np
#img=cv2.imread(r"C:\Users\Sneha\Pictures\Face.png") # to capture images
#cv2.imshow("output",img)
#cv2.waitKey(0)  #waits infinitely (0) and for 1000 ms or 1s (1000)
cap=cv2.VideoCapture(0)  #to capture video from webcam (0) and from file(1)
cap.set(3,640) #setting the width and height
cap.set(4,480)
while True:
    success,img=cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break