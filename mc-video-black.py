import cv2, time, os
from math import sqrt
from PIL import Image
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()
x,y,z = mc.player.getPos()
mc.player.setTilePos(x+50,y+30,z+50)
maxsize = (100, 100)
def getBlockFromColor(rgb):
    gray = int(0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2])
    if gray <= 64:
        return 49
    elif  64<gray <= 128:
        return (35,7)
    elif 128<gray<=192:
        return (35,8)
    else:
        return 35
# 在当前目录下新建文件夹
# 进行视频的载入
vc = cv2.VideoCapture('新宝岛.flv')
count = 0
# 判断载入的视频是否可以打开
ret = vc.isOpened()
# 循环读取视频帧
while ret:
    count +=  1
    # 进行单张图片的读取,ret的值为True或者Flase,frame表示读入的图片
    ret, frame = vc.read()
    if ret:
        # 存储为图像
        cv2.imwrite('temp.jpg', frame)
        # 输出图像名称
        print(f"第{count}帧")
        im = Image.open("temp.jpg") 
        im.thumbnail(maxsize, Image.ANTIALIAS)
        rgb_im = im.convert('RGB')
        rows, columns = rgb_im.size
        for r in range(rows):
            for c in range(columns):
                rgb = rgb_im.getpixel((r, c))
                mc_block = getBlockFromColor(rgb)
                mc.setBlock(x+r, y, z+c, mc_block)
        # 在一个给定的时间内(单位ms)等待用户按键触发,1ms
        #cv2.waitKey(1)
        #time.sleep(0.1)
    else:
        break
# 视频释放
vc.release()
