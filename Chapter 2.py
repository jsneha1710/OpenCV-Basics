import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
img=cv2.imread(r"C:\Users\Sneha\Pictures\Face.png")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#to capture images and convert to GrayScale image
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)#to capture Gray images and convert to Blurred image of size 7,7
imgCanny=cv2.Canny(img,100,100)#to capture images and convert to Canny image
imgdilate=cv2.dilate(img,kernel,iterations=1)#to capture images and convert to dilated image
imgerode=cv2.erode(imgdilate,kernel,iterations=1)#to capture images and convert to eroded image
cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blurry Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dilated Image",imgdilate)
cv2.imshow("Eroded Image",imgerode)

cv2.waitKey(0)