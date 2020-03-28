#将图像从一个色彩空间转换到另一个，向BGR<->灰色，BGR<->HSV
#学习cv.cvtColor,cv.inRange等
#cv.cvtColor(input_image,flag),其中flag决定转换的类型
#BGR->灰度转换，我们使用标志cv.COLOR_BGR2GRAY
#BGR->HSV转换，我们是用标志cv.COLOR_BGR2HSV
#BGR：基于三原色：[255,255,255]
#HSV：色度、饱和度、亮度： 色相范围[0,179],饱和度范围[0,255],值范围[0,255]