from PIL import ImageGrab
import time
import numpy as np
from PIL import Image
from ctypes import *

def local_s():
    # 21 53
    # 138 74
    im = ImageGrab.grab((21, 53, 138, 74))
    # im.show()
    # 保存地址 E:\mhxypic\local
    save_place = 'E:\mhxypic\local\loc'
    name_time = str(int(time.time()))
    im.save(save_place+name_time+'.tif')




def task_s():

    # im = ImageGrab.grab((489, 174, 625, 259))
    im = ImageGrab.grab((19, 46, 104, 107))
    # im = ImageGrab.grab((489, 174, 502, 188))
    # im.show()
    # 保存地址 E:\mhxypic\local

    # im = im.convert("L")
    # # im = im.convert("1")
    save_place = 'E:\mhxypic\mlocaltion/'
    name_time = str(int(time.time()))
    im.save(save_place + name_time + '.png')
    # im_arr = np.array(im)
    # # im.show()
    # print(im_arr)
    # with open('ss.txt','w+') as f:
    #     f.write(str(im_arr))
    # im = Image.open('E:\mhxypic\mtask\m2.png')
    #
    # Image_array = np.array(im)
    # print(Image_array)


def test():
    gdi32 = windll.gdi32
    user32 = windll.user32
    hdc = user32.GetDC(None)  # 获取颜色值
    pixel = gdi32.GetPixel(hdc, 489, 195)  # 提取RGB值
    r = pixel & 0x0000ff
    g = (pixel & 0x00ff00) >> 8
    b = pixel >> 16
    print([r, g, b])



if __name__ == '__main__':
    # local_s()
    task_s()
    # test()
