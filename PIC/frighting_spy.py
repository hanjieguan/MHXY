from PIL import ImageGrab
import numpy as np

def fright_or_not(x, y):
    im = ImageGrab.grab((x, y+204, x+3, y+476))
    # [[[248 248 216]]]
    Image_array = np.array(im)
    im.show()
    # print(Image_array)
    for Image_array_2d in Image_array:
        if np.array_equal(Image_array_2d, np.array([[248, 252, 248], [248, 252, 248], [248, 252, 248]])):
            pass
        else:
            pass
        print(Image_array_2d)
        print('                      ')

if __name__ == '__main__':
    fright_or_not(20, 16)