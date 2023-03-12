import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('/Users/kachai/PycharmProjects/HW-1/venv/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_default.xml')

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 读取摄像头中的图像
    ret, frame = cap.read()
    # A copy of frame store with"BGR"
    frame1= frame.copy()
    # 将图像转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #gray turn back into BGR
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    # Loop over each face and draw a rectangle around it
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(gray, (x, y), (x + w, y + h), (125, 120, 0),5)
        #crop and save the image
        face_color = frame[y:y + h, x:x + w]
        #sperate the BGR on the crop image
        B,G,R =cv2.split(face_color)
        #merge the crop the image into the background
        gray[y:y + h, x:x + w] = cv2.merge([B,G,R])
    #add the text
    cv2.putText(gray, 'MBS3523 Assignment 1-Q4    Name: Cheung Ka Chai', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 0), 3)
    # Display the resulting frame
    cv2.imshow('Face Detection',gray)

    # 按下esc键退出循环
    if cv2.waitKey(1) & 0xFF ==27:
        break

# 释放摄像头并关闭窗口
cap.release()
cv2.destroyAllWindows()