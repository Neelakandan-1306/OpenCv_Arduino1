import cv2
import controller as cnt
from cvzone.HandTrackingModule import HandDetector

detector=HandDetector(detectionCon=0.8,maxHands=1)

video=cv2.VideoCapture(0)

while True:
    ret,frame=video.read()
    frame=cv2.flip(frame,1)
    hands,img=detector.findHands(frame)
    if hands:
        lmList=hands[0]
        fingerUp=detector.fingersUp(lmList)

        print(fingerUp)
        cnt.led(fingerUp)
        count = 0
        for x in fingerUp:
            if x==1:
                count +=1
        cv2.putText(frame,f'Finger count:{count}',(20,460),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255),1,cv2.LINE_AA)

    cv2.imshow("frame",frame)
    if cv2.waitKey(1)==ord("q"):
        break

video.release()
cv2.destroyAllWindows()