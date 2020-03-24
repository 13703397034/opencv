#%%md
#访问和修改像素值
#加载彩色图像
import numpy as np
import cv2 as cv
img = cv.imread(r'C:\Users\guanlibu\Desktop\her\120.jpg',1)
#cv.imshow('123',img)
#可以通过行，列访问像素值，对于BGR图像，它返回一个由蓝色、绿色和红色值组成的数组，对于灰度图像，只返回相应的灰度
#返回值是像素点【100,100】处的蓝绿红三元素的值【232  144  60】
px =img[100,100]
print(px)
#仅返回该像素点蓝色的值
blue = img[100,100,0]
print(blue)
#可以通过赋值修改像素点的蓝绿红数组
img[100,100]=[255,255,255]
print(img[100,100])

#警告Numpy是用于快速数组计算的优化库，简单的访问每个像素值并对其修改非常缓慢，不建议使用
#对于单个像素访问使用array.item()和array.itemset()更好
img.item(10,10,2)
print(img.item(10,10,2))
img.itemset((10,10,2),100)
print(img.item(10,10,2))

#访问图像属性
#图像属性包含行数、列数、通道数、图像数据类型、像素数等
#图像的形状可通过img.shape访问。他返回行、列和通道数的元祖（如果图像是彩色的）
#如果图像是灰色的，返回的元祖只有行数和列数
print(img.shape)
#像素总数可以通过img.size访问
print(img.size)
#图像数据类型通过img.dtype获取
print(img.dtype)
#cv.waitKey(-1)
#