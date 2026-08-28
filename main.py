import cv2
import numpy as np
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture(0)
poseDetector = PoseDetector()
direction = 0
count = 0
while True:
    success, frame = cap.read()
    img=poseDetector.findPose(frame)
    lmList,bbox = poseDetector.findPosition(img,draw=False)
    if lmList:
       angle,img = poseDetector.findAngle(
           lmList[12][0:2],
           lmList[14][0:2],
           lmList[16][0:2],
           img=img
       )
       xp=(340,200)
       fp_per=(0,100)
       per = np.interp(angle,xp,fp_per)
       
       if per == 100:
           if direction == 0:
               direction = 1
       if per == 0:
           if direction == 1:
               count+=1
               direction = 0

       cv2.putText(img,str(int(count)),(200,200),cv2.FONT_HERSHEY_PLAIN,4,(255,0,0),4)
       cv2.putText(img,f"{int(per)}%",(50,400),cv2.FONT_HERSHEY_PLAIN,4,(255,0,0),4)
       cv2.rectangle(img,(550,50),(620,400),(0,255,0),3)
       bar = np.interp(per,(0,100),(400,50))
       cv2.rectangle(img,(550,int(bar)),(620,400),(0,255,0),cv2.FILLED)
    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
