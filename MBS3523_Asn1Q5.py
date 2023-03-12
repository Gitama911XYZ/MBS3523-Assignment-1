import cv2
import numpy as np
def position (pos):
     pass

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

cv2.namedWindow("TrackBar")

cv2.createTrackbar("x-axix","TrackBar",0,640,position)
cv2.createTrackbar("y-axix","TrackBar",0,480,position)
while (True):
    rat,frame=cap.read()
    x=cv2.getTrackbarPos("x-axix","TrackBar")
    y=cv2.getTrackbarPos("y-axix","TrackBar")
    cv2.line(frame, (x, 0), (x, 480), (0, 255, 0), 2)
    cv2.line(frame,(0,y),(640,y),(255, 0, 0), 2)
    cv2.putText(frame, 'MBS3523 Assignment 1-Q5    Name: Cheung Ka Chai', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(150, 0, 0), 2)
    cv2.imshow("TrackBar", frame)
    if cv2.waitKey(1) & 0xFF == 27: #esc
        break

cap.release()
cv2.destroyAllWindows()