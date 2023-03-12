import cv2
import numpy as np
import random

# 初始化摄像头
capture = cv2.VideoCapture(0)

# 定义窗口宽度和高度
frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 初始化框的位置和速度
x = random.randint(0, frame_width - 80)
y = random.randint(0, frame_height - 80)
angle = random.randint(15, 75)
velocityX = 5 * np.cos(angle * np.pi / 180)
velocityY = 5 * np.sin(angle * np.pi / 180)

# 定义方框的颜色和大小
color = (0, 255, 0)
box_size = 80

# 无限循环，直到用户按下"q"键退出程序
while True:
    # 从摄像头读取帧
    ret, webCam = capture.read()

    # 如果无法读取帧，则退出循环
    if not ret:
        break

    # 计算下一步的位置
    x += velocityX
    y += velocityY

    # 如果框超出边界，则改变速度
    if x < 0 or x > frame_width - box_size:
        velocityX = -velocityX
    if y < 0 or y > frame_height - box_size:
        velocityY = -velocityY

    # 绘制框
    cv2.rectangle(webCam, (int(x), int(y)), (int(x + box_size), int(y + box_size)), color, 2)

    cv2.putText(webCam, 'MBS3523 Assignment 1-Q3    Name: Cheung Ka Chai', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (125, 120, 0), 3)
    # 显示帧
    cv2.imshow('frame', webCam)

    # 如果用户按下"esc"键，则退出程序
    if cv2.waitKey(1) & 0xFF == 27:
        break

# 释放摄像头并关闭窗口
capture.release()
cv2.destroyAllWindows()