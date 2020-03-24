import  numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
#定义编解码器并创建VideoWriter对象
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi',fourcc,20.0,(640,480))
while cap.isOpened():
    ret ,frame = cap.read()
    if not ret:
        print("获取不到视频退出")
        break
    #frame =cv.flip(frame,0)
    #写翻转的框架
    out.write(frame)
    cv.imshow('frame',frame)
    if cv.waitKey(1) == ord('q'):
        break
#完成工作释放所有内容
cap.release()
out.release()
cv.destroyAllWindows()
