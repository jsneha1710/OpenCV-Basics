import cv2
import numpy as np
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
#img=cv2.imread(r"C:\Users\Sneha\Pictures\Face.png")
#imgStack=stackImages(0.5,([img,img,img]))
#cv2.imshow("ImageStack",imgStack)

def getcontours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)
        if(area>500):
            cv2.drawContours(imgcontour,cnt,-1,(255,0,0),1)
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            objcorner=len(approx)
            x ,y ,w ,h=cv2.boundingRect(approx)
            if(objcorner==3):
                objtype="Triangle"
            elif(objcorner==4):
                aspratio=w/float(h)
                if(aspratio>0.95 and aspratio<1.05):
                    objtype="Square"
                else:
                    objtype="Rectangle"
            elif (objcorner==6):
                objtype = "Hexagon"
            elif(objcorner>6):
                objtype="Circle"
            else:
                objtype="None"

            cv2.rectangle(imgcontour,(x,y),(x+w,y+h),(0,255,0),1)
            cv2.putText(imgcontour,objtype,((x+(w//2)-10),(y+(h//2)-10)),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),2)



img=cv2.imread(r"C:\Users\Sneha\Pictures\shapes1.png")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#to capture images and convert to GrayScale image
imgBlur=cv2.GaussianBlur(imgGray,(7,7),1)#to capture Gray images and convert to Blurred image of size 7,7
imgCanny=cv2.Canny(imgBlur,50,50)
imgcontour=img.copy()
imgblank=np.zeros_like(img)
getcontours(imgCanny)
imgstack=stackImages(1,([img,imgGray,imgBlur],[imgCanny,imgcontour,imgblank]))
cv2.imshow("Stacked Images",imgstack)


cv2.waitKey(0)