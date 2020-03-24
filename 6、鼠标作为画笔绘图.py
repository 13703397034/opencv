'''
学习处理鼠标事件cv.setMouseCallback()
'''
import cv2 as cv
#鼠标回调函数的创建
events = [i for i in dir(cv) if 'EVENT' in i]
print(events)
#鼠标回调函数在双击的地方绘制一个正方形
import numpy as np
import cv2 as cv
#鼠标回调函数

#def draw_circle(enevt, x, y, flags, param):
#    if event ==cv.EVENT_LBUTTONDBLCLK:
 #       cv.circle(img,(x,y),100,(255,0,0),-1)
#创建一个黑色的图像，一个窗口并绑定到窗口的功能
#img =np.zeros((512,512,3),np.uint8)
#cv.namedWindow('image')
#cv.setMouseCallback('img',draw_circle)
#while(1):
#    cv.imshow('image',img)
 #   if cv.waitKey(20) & 0xFF == 27:
#        break
#cv.destroyAllWindows()
