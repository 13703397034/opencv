import cv2 as cv
import numpy as np
import os
#按照路径读取照片，取参数cv.IMREAD_REDUCED_COLOR加载彩色图像
                #取参数cv.IMREAD_REDUCED_GRAYSCALE 加载灰度模式
#设置文件夹位置变量
path = r'C:\Users\guanlibu\Desktop\her'
#遍历文件夹文件获取文件名称的集合
dirs = os.listdir(path)
#遍历文件名称集合
for file in dirs:
    #打印文件路径
    print(path+'\\'+file)
    #打印文件名
    print(os.path.basename(file)[0:-4])
    #将文件转灰后赋值img
    img = cv.imread(path+'\\'+file,cv.IMREAD_REDUCED_GRAYSCALE_2)
#将读取的照片展示在windows窗口，必须有窗口名，窗口自己适应照片尺寸
    cv.imshow('syt',img)
#可以设置一个空窗口，包含窗口名和一个参数cv.WINDOW_AUTOSIZE代表空窗口不允许拉伸,
# cv.WINDOW_NORMAL代表空窗口可以拉伸
    cv.namedWindow('kong',cv.WINDOW_AUTOSIZE)
    cv.imshow('kong',img)
#cv.imwrite()存储照片，第一个参数为路径/照片名和格式，第二个参数为要保存的对象
#cv.imwrite('first.png',img)
#设置键盘等待时间，参数为0 表示循环显示，直到键盘输入返回键盘输入的值。
    k = cv.waitKey(0)
    if k == 27:    #按ESC键销毁窗口
    #销毁所有windows窗口
        cv.destroyAllWindows()
    elif k == ord('s'):#键盘输入s 保存照片,并销毁窗口
        cv.imwrite('bc.png',img)
        cv.destroyAllWindows()
