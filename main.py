import pickle
import sqlite3
import time
import cv2
import cvzone
import numpy as np

con = sqlite3.connect('/home/ufaz/Desktop/Parking/parking/db.sqlite3')
cur = con.cursor()

# Video feed
# link='http://192.168.0.108:4747/video'
cap = cv2.VideoCapture('carPark.mp4')
# cap = cv2.VideoCapture(0)
 
with open('CarParkPos2', 'rb') as f:
    posList = pickle.load(f)
 
# width, height = 250,130
width, height = 105,42
 
def checkParkingSpace(imgPro):
    spaceCounter = 0
    i=1
    n=0
    A=[1,1,1]
    B=[1,1,1]
    for pos in posList:
        x, y = pos
 
        imgCrop = imgPro[y:y + height, x:x + width]
        # cv2.imshow(str(x * y), imgCrop)
        count = cv2.countNonZero(imgCrop)
        if count < 900:
            color = (0, 255, 0)
            thickness = 3
            spaceCounter += 1
            if n==0:
                A[i-1]=1
            elif n==1:
                B[i-1]=1
        else:
            color = (0, 0, 255)
            thickness = 2
            if n==0:
                A[i-1]=0
            elif n==1:
                B[i-1]=0
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1,
                           thickness=2, offset=3, colorR=color)
        i+=1
        if i==4:
            i=1
            n+=1
    AL=''
    BL=''
    if A.count(1)==0:
        AL='FULL'
    elif A.count(1)==3:
        AL='All places are free'
    else:
        for i in range(0,3):
            if A[i]==1:
                kA=i+1
                AL+=str(kA)
                AL+=' ; '

    if B.count(1)==0:
        BL='FULL'
    elif B.count(1)==3:
        BL='All places are free'
    else:
        for j in range(0,3):
            if B[j]==1:
                kB=j+1
                BL+=str(kB)
                BL+=' ; '
    
       
            
    
       
            
            
    cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=2,
                           thickness=2, offset=10, colorR=(0,200,0))
    cvzone.putTextRect(img, 'ROW A', (350, 30), scale=2,
                           thickness=2, offset=6, colorR=(0,300,0))
    cvzone.putTextRect(img, 'ROW B', (740, 30), scale=2,
                           thickness=2, offset=6, colorR=(0,300,0))
    con.execute(f"UPDATE SmartParking_room set FREE_PLACES = {spaceCounter} , PLACES = {len(posList)} , ORDER_A = '{AL}' , ORDER_B = '{BL}'  where ID = 1")
    con.commit()

   
       
        
while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)
    checkParkingSpace(imgDilate)
    cv2.imshow("Video", img)
    cv2.waitKey(10)
