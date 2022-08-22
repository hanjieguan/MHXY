from PIL import Image
from PIL import ImageGrab
import aircv as ac
from pynput.mouse import Button, Controller
import os
import numpy as np
import click_xiaoer_pic as cxe
import time
def test():
    while True:
        imsrc = np.array(ImageGrab.grab((0, 0, 610, 517)))
        for root, dirs, files in os.walk('E:\mhxypic\dianxiaoer/'):
            for file in files:
                im = Image.open(r'E:\mhxypic\dianxiaoer/' + file)
                Image_array = np.array(im)
                match_result = ac.find_template(imsrc,np.array(Image_array), 0.8)
                if match_result is not None:
                    print(match_result)
        time.sleep(0.2)


def test2():
    for root, dirs, files in os.walk('E:\mhxypic\dianxiaoer/'):
        for file in files:
            im = Image.open(r'E:\mhxypic\dianxiaoer/' + file)
            Image_array = np.array(im)
            font_test_list3 = []
            for font_array_2d in Image_array:
                font_test_list2 = []
                for font_array_1d in font_array_2d:
                    font_test_list1 = []
                    for font_array_1d_element in font_array_1d:
                        font_test_list1.append(font_array_1d_element)
                    font_test_list2.append(font_test_list1)
                font_test_list3.append(font_test_list2)
            print(file + ' = ' + str(font_test_list3))





if __name__ == '__main__':
    test()