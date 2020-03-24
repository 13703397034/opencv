'''
学习读取视频、显示视频、保存视频
从相机中捕捉并显示它
学习以下功能 cv.VideoCapture(),cv.VideoWriter()
'''
#从相机中读取视频，创建一个VideoCapture对象。它的参数是设备索引或者视频文件的名称，
#设备索引是指定哪个摄像头，一个摄像头连接是我们输入0或-1，第二个摄像头输入1，以此类推
#最后释放他们
import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("cannot open camera")
    exit()
while True:
    #逐帧捕获图片
    ret , frame = cap.read()
    #如果正确读取帧，ret为True
    if not ret:
        print("读取帧失败")
        break
    #在框架上的操作到这里（图像转灰）
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    #显示结果帧q

    cv.imshow('frame',gray)
    if cv.waitKey(1) == ord('q'):
        break
#完成捕捉释放捕获器
cap.release()
cv.destroyAllWindows()