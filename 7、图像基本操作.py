#访问和修改像素值
#加载彩色图像
import numpy as np
import cv2 as cv
img = cv.imread(r'C:\Users\guanlibu\Desktop\her\120.jpg',1)

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

#图像感兴趣区域ROI
#可以提高准确性和性能，可以将球的复制到其他区域
ball = img[280:340,330:390]#将一个区域赋值给ball
img [273:333,100:160] = ball#将ball赋值给另一个区域，区域大小一致

#拆分和合并图像通道
b,g,r = cv.split(img)#拆分通道是一个耗时的操作，一般时候需要使用numpy索引
img = cv.merge((b,g,r))
b = img[:,:,0]
img[:,:,2]=0
r = img[:,:,2]
print(r)

#为图像设置边框（填充）
'''
使用cv.copyMakeBorder()创建图像周围的边框，在卷积运算和零填充方面应用较多
此函数采用的参数如下
src 输入图像
top,bottom,left,right 边界宽度（以相应方向上的像素为单位）
borderType 定义要添加哪种边框的标志。他可以是一下类型：
    cv.BORDER_CONSTANT 添加恒定的彩色边框。该值作为下一个参数给出
    cv.BORDER_REFLECT 边框将是边框元素的镜像（fedcba/abcdef）
    cv.BORDER_REFLECT_101或cv.BORDER_DEFAULT 与上述相同,略有变化
    cv.BORDER_REPLICATE 最后一个元素被复制（abcdef/fffff）
    value 边框的颜色，如果边框类型为cv.BORDER_CONSTANT时使用
    
'''
RED =[0,0,255]
constant = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_CONSTANT,value =RED)
cv.imshow('123',constant)
cv.waitKey(-1)
