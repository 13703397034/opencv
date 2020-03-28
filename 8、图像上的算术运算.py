'''
学习图像的几种算术运算，加法、减法、按位运算
学习cv.add,cv.addWeighted
'''
#opencv 的函数cv.add()或仅通过numpy操作res = img1+ img2添加两个图像，
# 两个图像应具有相同的深度和类型，或者第二个图像可以只是一个标量值

#Opencv的加法是饱和运算，Numpy加法是模运算
import cv2 as cv
import numpy as np
'''
x = np.uint8([250])
y = np.uint8([20])
print(cv.add(x,y))# 255+10 = 260 =>255最大值255
print(x+y)#250+10 = 260%256 =4
#opencv的add（）函数能提供更好的结果，最好坚持使用opencv 功能
'''
'''
#图像融合
#图像融合也是图像加法，但对图像赋予不同的权重，以使其具有融合或透明的感觉
#等式为：$$G(x)=(1-\alpha)f_0(x)+\alphaf_1(x)$$
#通过从$\alpha$从$0\rightarrow1$更改，可以在一个图像到另一个图像之间执行很酷的过渡
#拍摄两个图片将他们融合第一幅权重为0.7，第二幅权重为0.3。cv.addWeighted()。公式 如下
#$$dst = \alpha\cdot img1+\beta\cdot img2gamma$$,在这里$\gamma$被视为零
img1 = cv.imread('110.jpg')
img2 = cv.imread('120.jpg')
dst = cv.addWeighted(img1,0.7,img2,0.3,0)
cv.imshow('new',dst)
cv.waitKey(0)
cv.destroyAllWindows()
'''

#按位运算
#按位运算（AND,OR,NOT,XOR）操作，他们在提取部分图像，定义和处理非矩形ROI等方面非常有用


