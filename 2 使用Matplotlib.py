'''
Matplotlib是Python的绘图库，可为你提供多种绘图方法。
使用Matplotlib显示图像。你可以使用Matplotlib缩放图像，保存图像等。
'''
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread(r'C:\Users\guanlibu\Desktop\her\120.jpg',1)
plt.imshow(img,cmap='gray',interpolation='bicubic')#打开图片
plt.xticks([])#隐藏X轴的刻度值
plt.yticks([])#隐藏Y轴的刻度值
plt.show()
