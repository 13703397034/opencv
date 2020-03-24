'''
学习使用opencv绘制不同的几何图形
学习以下功能：cv.line() cv.circle() cv.rectangle() cv.ellipse()
 cv.putText()
img:代表要绘制形状的图像
color：形状的颜色。（255,0,0）对于灰度只需传递标量即可
厚度：线或圆的粗细。如多对闭合图形（如圆）传递-1，它将填充形状。默认厚度等于1
lineType:线的类型，是否为8连接线。默认为8连接线，cv.LINE__AA是抗锯齿线
'''
#要绘制一条线，需要传递线的开始和结束坐标
import  numpy as np
import cv2 as cv
#创建黑色的图像
img = np.zeros((512,512,3),np.uint8)
#绘制一条厚度为5的蓝色对角线
cv.line(img , (0,0),(511,511),(255,0,0),5)
#在图片右上角画一个矩形
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)
#在矩形内绘制一个圆圈
cv.circle(img,(447,63),63,(0,0,255),-1)
#绘制一个椭圆中心位置参数（x,y）轴长度（长轴长度，短轴长度）
cv.ellipse(img,(256,256),(100,50),0,0,360,255,-1)
#绘制多边形
pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))
#向图像中添加文本
#参数（img，放置的位置图标即数据开始的左下角，text内容，字体类型，字体大小，颜色，厚度，线条等）为了更好的美观建议使用lineType=cv.LINE_AA)
#font 是字体类型
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OPENCV',(10,500),font,4,(255,255,255),2,cv.LINE_AA)
#输出图像
cv.imshow("tuxiang",img)
cv.waitKey(0)
cv.destroyAllWindows()