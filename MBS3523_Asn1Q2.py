import cv2


cam = cv2.VideoCapture(0)

while (True):

    (ret, image) = cam.read()
    BW = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',image)
    cv2.imshow('B&W', BW)
    if cv2.waitKey(1) & 0xff == 27:
        break
cam.release()
cv2.destroyAllWindows()