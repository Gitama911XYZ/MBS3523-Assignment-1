import cv2

evt = 0
pntStart = [0, 0]
pntEnd = [0, 0]
lastPnt = 0
ix, iy = 0, 0
x1, y1, x2, y2 = 0, 0, 0, 0


def myFun(event, xpos, ypos, flags, paream):
    global evt
    global pntStart
    global pntEnd
    global x1, y1, x2, y2, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)
        evt = event
        pntStart = (xpos, ypos)
        ix, iy = xpos, ypos
    if event == cv2.EVENT_LBUTTONUP:
        print(event)
        evt = event
        pntEnd = (xpos, ypos)
        pntEnd = xpos, ypos
        x1, y1 = ix, iy
        x2, y2 = xpos, ypos

    if event == cv2.EVENT_RBUTTONDOWN:
        print(event)
        evt = event


cam = cv2.VideoCapture(0)
cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame', myFun)

while True:
    ret, frame = cam.read()

    if evt == 4:
        if pntStart != pntEnd:
            frameROI = frame[pntStart[1]:pntEnd[1], pntStart[0]:pntEnd[0]]
            if lastPnt != (pntStart, pntEnd) and lastPnt != 0:
                cv2.destroyWindow('ROI FRAME')
            lastPnt = (pntStart, pntEnd)
            cv2.rectangle(frameROI, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(frame, (pntStart[0], pntStart[1]), (pntEnd[0], pntEnd[1]), (0, 255, 0), 2)
            cv2.imshow('ROI FRAME', frameROI)
    elif evt == 2:
        cv2.destroyWindow('ROI FRAME')
        lastPnt = 0
        x1, y1 = 0, 0
        x2, y2 = 0, 0

    cv2.putText(frame, 'MBS3523 Assignment 1-Q6    Name: Cheung Ka Chai',
                (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (150, 0, 0), 3)
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()
