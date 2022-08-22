import numpy as np
import localtion_spy_font
# import localtion_spy_font
from PIL import ImageGrab
# import time
# from PIL import Image
# import os

def localtion_getter(x, y):
    # 初始场景文字个数
    local_name_nums = 0
    # 最终想要得到的场景
    localtion_now = None
    # 坐标
    local_x = 0
    local_y = 0
    local_x_list = []
    local_y_list = []
    # 坐标错误标志
    local_pos_wrong_mark = 0
    # 坐标y字是否被找到标志
    local_pos_y_or_not = False
    im = ImageGrab.grab((x+19, y+46, x+104, y+107))
    Image_array = np.array(im)
    try:
        try:
            for local_start_column in range(3, 78):
                local_name_thitck = Image_array[0:14, local_start_column - 1:local_start_column]
                for local_name_thitck_element in local_name_thitck:
                    # 先找到第一个白色
                    if not np.array_equal(local_name_thitck_element, np.array([[255, 255, 255]])):
                        pass
                    else:
                        raise Exception
        except Exception:
            while True:
                # 是否有文字
                local_or_not = False
                local_name_thitck = Image_array[0:14, local_start_column - 1:local_start_column]
                for local_name_thitck_element in local_name_thitck:
                    if np.array_equal(local_name_thitck_element, np.array([[255, 255, 255]])) or np.array_equal(
                            local_name_thitck_element, np.array([[0, 0, 0]])):
                        local_or_not = True
                        break
                    # 此时表示 在第一次遇到白色之后，后面的几次获取字体颜色失败，即表示后面已经没有字了
                    else:
                        pass

                if local_or_not is True:
                    local_name_nums += 1
                    if local_name_nums == 1:
                        first_font = Image_array[0:8, local_start_column - 1:local_start_column + 12]
                        font_test_list3 = []
                        for font_array_2d in first_font:
                            font_test_list2 = []
                            for font_array_1d in font_array_2d:
                                if not np.array_equal(font_array_1d, np.array([255, 255, 255])):
                                    font_test_list1 = [0, 0, 0]
                                else:
                                    font_test_list1 = [255, 255, 255]
                                font_test_list2.append(font_test_list1)
                            font_test_list3.append(font_test_list2)
                        # 判断是否在第一个字列表中，若不在，则退出循环，报告错误地址
                        if font_test_list3 in localtion_spy_font.First_font_list:
                            local_start_column = local_start_column + 16
                            first_font = font_test_list3
                        else:
                            raise KeyboardInterrupt
                    elif local_name_nums == 2:
                        second_font = Image_array[0:8, local_start_column - 1:local_start_column + 12]
                        font_test_list3 = []
                        for font_array_2d in second_font:
                            font_test_list2 = []
                            for font_array_1d in font_array_2d:
                                if not np.array_equal(font_array_1d, np.array([255, 255, 255])):
                                    font_test_list1 = [0, 0, 0]
                                else:
                                    font_test_list1 = [255, 255, 255]
                                font_test_list2.append(font_test_list1)
                            font_test_list3.append(font_test_list2)
                        if font_test_list3 in localtion_spy_font.Second_font_list:
                            if (first_font + font_test_list3) in localtion_spy_font.Two_word_list:
                                second_font = font_test_list3
                                local_start_column = local_start_column + 16
                            else:
                                raise KeyboardInterrupt
                        else:
                            raise KeyboardInterrupt
                    elif local_name_nums == 3:
                        three_font = Image_array[0:8, local_start_column - 1:local_start_column + 12]
                        font_test_list3 = []
                        for font_array_2d in three_font:
                            font_test_list2 = []
                            for font_array_1d in font_array_2d:
                                if not np.array_equal(font_array_1d, np.array([255, 255, 255])):
                                    font_test_list1 = [0, 0, 0]
                                else:
                                    font_test_list1 = [255, 255, 255]
                                font_test_list2.append(font_test_list1)
                            font_test_list3.append(font_test_list2)
                        if font_test_list3 in localtion_spy_font.Three_font_list:
                            if (first_font + second_font + font_test_list3) in localtion_spy_font.Three_word_list:
                                three_font = font_test_list3
                                local_start_column = local_start_column + 16
                            else:
                                raise KeyboardInterrupt
                        else:
                            raise KeyboardInterrupt
                    elif local_name_nums == 4:
                        four_font = Image_array[0:8, local_start_column - 1:local_start_column + 12]
                        font_test_list3 = []
                        for font_array_2d in four_font:
                            font_test_list2 = []
                            for font_array_1d in font_array_2d:
                                if not np.array_equal(font_array_1d, np.array([255, 255, 255])):
                                    font_test_list1 = [0, 0, 0]
                                else:
                                    font_test_list1 = [255, 255, 255]
                                font_test_list2.append(font_test_list1)
                            font_test_list3.append(font_test_list2)
                        if font_test_list3 in localtion_spy_font.Four_font_list:
                            if (
                                    first_font + second_font + three_font + font_test_list3) in localtion_spy_font.Four_word_list:
                                four_font = font_test_list3
                                local_start_column = local_start_column + 16
                            else:
                                raise KeyboardInterrupt
                        else:
                            raise KeyboardInterrupt
                    # 出现第五个字，错误
                    else:
                        raise KeyboardInterrupt
                else:
                    if local_name_nums == 0:
                        raise KeyboardInterrupt
                    elif local_name_nums == 2:
                        # 此时只可能是 地府
                        localtion_now = '地府'
                        # 检测X坐标
                        for local_pos in range(18, 42, 8):
                            if len(local_x_list) == 0:
                                local_pos_font = Image_array[51:61, local_pos:local_pos + 8]
                                font_test_list3 = []
                                for font_array_2d in local_pos_font:
                                    font_test_list2 = []
                                    for font_array_1d in font_array_2d:
                                        if not np.array_equal(font_array_1d, np.array([255, 255, 255])):
                                            font_test_list1 = [0, 0, 0]
                                        else:
                                            font_test_list1 = [255, 255, 255]
                                        font_test_list2.append(font_test_list1)
                                    font_test_list3.append(font_test_list2)
                                if font_test_list3 in localtion_spy_font.Num_pos_list:
                                    local_x_list.append(localtion_spy_font.Num_pos_wenzi_list[
                                                            localtion_spy_font.Num_pos_list.index(font_test_list3)])
                                else:
                                    local_pos_wrong_mark = 1
                                    break
                            else:
                                local_pos_font = Image_array[51:61, local_pos:local_pos + 8]
                                font_test_list3 = []
                                for font_array_2d in local_pos_font:
                                    font_test_list2 = []
                                    for font_array_1d in font_array_2d:
                                        if not np.array_equal(font_array_1d, np.array([255, 255, 255])):
                                            font_test_list1 = [0, 0, 0]
                                        else:
                                            font_test_list1 = [255, 255, 255]
                                        font_test_list2.append(font_test_list1)
                                    font_test_list3.append(font_test_list2)
                                if font_test_list3 in localtion_spy_font.Num_pos_list:
                                    local_x_list.append(localtion_spy_font.Num_pos_wenzi_list[
                                                            localtion_spy_font.Num_pos_list.index(font_test_list3)])
                                else:
                                    break

                        # 检测 y字符
                        for local_pos in range(44, 55):
                            if local_pos_y_or_not is False:
                                local_pos_font = Image_array[51:61, local_pos:local_pos + 1]
                                for local_pos_font_element in local_pos_font:
                                    if np.array_equal(local_pos_font_element, np.array([[255, 255, 255]])):
                                        local_pos_y_or_not = True
                                        break
                                    else:
                                        pass
                            else:
                                break
                        else:
                            local_pos_wrong_mark = 1

                        local_pos = local_pos - 1
                        local_pos_font = Image_array[51:61, local_pos: local_pos + 7]

                        font_test_list3 = []
                        for font_array_2d in local_pos_font:
                            font_test_list2 = []
                            for font_array_1d in font_array_2d:
                                if not np.array_equal(font_array_1d, np.array([255, 255, 255])):
                                    font_test_list1 = [0, 0, 0]
                                else:
                                    font_test_list1 = [255, 255, 255]
                                font_test_list2.append(font_test_list1)
                            font_test_list3.append(font_test_list2)
                        if font_test_list3 == localtion_spy_font.P_y:
                            # 次数检测y坐标
                            local_pos = local_pos + 15
                            for local_pos in range(local_pos, local_pos + 24, 8):
                                if len(local_y_list) == 0:
                                    local_pos_font = Image_array[51:61, local_pos:local_pos + 8]
                                    font_test_list3 = []
                                    for font_array_2d in local_pos_font:
                                        font_test_list2 = []
                                        for font_array_1d in font_array_2d:
                                            if not np.array_equal(font_array_1d, np.array([255, 255, 255])):
                                                font_test_list1 = [0, 0, 0]
                                            else:
                                                font_test_list1 = [255, 255, 255]
                                            font_test_list2.append(font_test_list1)
                                        font_test_list3.append(font_test_list2)
                                    if font_test_list3 in localtion_spy_font.Num_pos_list:
                                        local_y_list.append(localtion_spy_font.Num_pos_wenzi_list[
                                                                localtion_spy_font.Num_pos_list.index(
                                                                    font_test_list3)])
                                    else:
                                        local_pos_wrong_mark = 1
                                        break
                                else:
                                    local_pos_font = Image_array[51:61, local_pos:local_pos + 8]
                                    font_test_list3 = []
                                    for font_array_2d in local_pos_font:
                                        font_test_list2 = []
                                        for font_array_1d in font_array_2d:
                                            if not np.array_equal(font_array_1d, np.array([255, 255, 255])):
                                                font_test_list1 = [0, 0, 0]
                                            else:
                                                font_test_list1 = [255, 255, 255]
                                            font_test_list2.append(font_test_list1)
                                        font_test_list3.append(font_test_list2)
                                    if font_test_list3 in localtion_spy_font.Num_pos_list:
                                        local_y_list.append(localtion_spy_font.Num_pos_wenzi_list[
                                                                localtion_spy_font.Num_pos_list.index(
                                                                    font_test_list3)])
                                    else:
                                        break
                        else:
                            local_pos_wrong_mark = 1
                        if local_pos_wrong_mark == 1:
                            local_x_list = [-1, -1, -1]
                            local_y_list = [-1, -1, -1]
                        else:
                            pass
                        raise SystemExit
                    elif local_name_nums == 3:
                        localtion_now = localtion_spy_font.All_place_wenzi_list[
                            localtion_spy_font.All_place_list.index(first_font + second_font + three_font)]
                        # 检测X坐标
                        for local_pos in range(18, 42, 8):
                            if len(local_x_list) == 0:
                                local_pos_font = Image_array[51:61, local_pos:local_pos + 8]
                                font_test_list3 = []
                                for font_array_2d in local_pos_font:
                                    font_test_list2 = []
                                    for font_array_1d in font_array_2d:
                                        if not np.array_equal(font_array_1d, np.array([255, 255, 255])):
                                            font_test_list1 = [0, 0, 0]
                                        else:
                                            font_test_list1 = [255, 255, 255]
                                        font_test_list2.append(font_test_list1)
                                    font_test_list3.append(font_test_list2)
                                if font_test_list3 in localtion_spy_font.Num_pos_list:
                                    local_x_list.append(localtion_spy_font.Num_pos_wenzi_list[
                                                            localtion_spy_font.Num_pos_list.index(font_test_list3)])
                                else:
                                    local_pos_wrong_mark = 1
                                    break
                            else:
                                local_pos_font = Image_array[51:61, local_pos:local_pos + 8]
                                font_test_list3 = []
                                for font_array_2d in local_pos_font:
                                    font_test_list2 = []
                                    for font_array_1d in font_array_2d:
                                        if not np.array_equal(font_array_1d, np.array([255, 255, 255])):
                                            font_test_list1 = [0, 0, 0]
                                        else:
                                            font_test_list1 = [255, 255, 255]
                                        font_test_list2.append(font_test_list1)
                                    font_test_list3.append(font_test_list2)
                                if font_test_list3 in localtion_spy_font.Num_pos_list:
                                    local_x_list.append(localtion_spy_font.Num_pos_wenzi_list[
                                                            localtion_spy_font.Num_pos_list.index(font_test_list3)])
                                else:
                                    break

                        # 检测 y字符
                        for local_pos in range(44, 55):
                            if local_pos_y_or_not is False:
                                local_pos_font = Image_array[51:61, local_pos:local_pos + 1]
                                for local_pos_font_element in local_pos_font:
                                    if np.array_equal(local_pos_font_element, np.array([[255, 255, 255]])):
                                        local_pos_y_or_not = True
                                        break
                                    else:
                                        pass
                            else:
                                break
                        else:
                            local_pos_wrong_mark = 1

                        local_pos = local_pos - 1
                        local_pos_font = Image_array[51:61, local_pos: local_pos + 7]

                        font_test_list3 = []
                        for font_array_2d in local_pos_font:
                            font_test_list2 = []
                            for font_array_1d in font_array_2d:
                                if not np.array_equal(font_array_1d, np.array([255, 255, 255])):
                                    font_test_list1 = [0, 0, 0]
                                else:
                                    font_test_list1 = [255, 255, 255]
                                font_test_list2.append(font_test_list1)
                            font_test_list3.append(font_test_list2)
                        if font_test_list3 == localtion_spy_font.P_y:
                            # 次数检测y坐标
                            local_pos = local_pos + 15
                            for local_pos in range(local_pos, local_pos + 24, 8):
                                if len(local_y_list) == 0:
                                    local_pos_font = Image_array[51:61, local_pos:local_pos + 8]
                                    font_test_list3 = []
                                    for font_array_2d in local_pos_font:
                                        font_test_list2 = []
                                        for font_array_1d in font_array_2d:
                                            if not np.array_equal(font_array_1d, np.array([255, 255, 255])):
                                                font_test_list1 = [0, 0, 0]
                                            else:
                                                font_test_list1 = [255, 255, 255]
                                            font_test_list2.append(font_test_list1)
                                        font_test_list3.append(font_test_list2)
                                    if font_test_list3 in localtion_spy_font.Num_pos_list:
                                        local_y_list.append(localtion_spy_font.Num_pos_wenzi_list[
                                                                localtion_spy_font.Num_pos_list.index(
                                                                    font_test_list3)])
                                    else:
                                        local_pos_wrong_mark = 1
                                        break
                                else:
                                    local_pos_font = Image_array[51:61, local_pos:local_pos + 8]
                                    font_test_list3 = []
                                    for font_array_2d in local_pos_font:
                                        font_test_list2 = []
                                        for font_array_1d in font_array_2d:
                                            if not np.array_equal(font_array_1d, np.array([255, 255, 255])):
                                                font_test_list1 = [0, 0, 0]
                                            else:
                                                font_test_list1 = [255, 255, 255]
                                            font_test_list2.append(font_test_list1)
                                        font_test_list3.append(font_test_list2)
                                    if font_test_list3 in localtion_spy_font.Num_pos_list:
                                        local_y_list.append(localtion_spy_font.Num_pos_wenzi_list[
                                                                localtion_spy_font.Num_pos_list.index(
                                                                    font_test_list3)])
                                    else:
                                        break
                        else:
                            local_pos_wrong_mark = 1
                        if local_pos_wrong_mark == 1:
                            local_x_list = [-1, -1, -1]
                            local_y_list = [-1, -1, -1]
                        else:
                            pass
                        raise SystemExit
                    elif local_name_nums == 4:
                        localtion_now = localtion_spy_font.All_place_wenzi_list[
                            localtion_spy_font.All_place_list.index(first_font + second_font + three_font + four_font)]
                        # 检测X坐标
                        for local_pos in range(18, 42, 8):
                            if len(local_x_list) == 0:
                                local_pos_font = Image_array[51:61, local_pos:local_pos + 8]
                                font_test_list3 = []
                                for font_array_2d in local_pos_font:
                                    font_test_list2 = []
                                    for font_array_1d in font_array_2d:
                                        if not np.array_equal(font_array_1d, np.array([255, 255, 255])):
                                            font_test_list1 = [0, 0, 0]
                                        else:
                                            font_test_list1 = [255, 255, 255]
                                        font_test_list2.append(font_test_list1)
                                    font_test_list3.append(font_test_list2)
                                if font_test_list3 in localtion_spy_font.Num_pos_list:
                                    local_x_list.append(localtion_spy_font.Num_pos_wenzi_list[
                                                            localtion_spy_font.Num_pos_list.index(font_test_list3)])
                                else:
                                    local_pos_wrong_mark = 1
                                    break
                            else:
                                local_pos_font = Image_array[51:61, local_pos:local_pos + 8]
                                font_test_list3 = []
                                for font_array_2d in local_pos_font:
                                    font_test_list2 = []
                                    for font_array_1d in font_array_2d:
                                        if not np.array_equal(font_array_1d, np.array([255, 255, 255])):
                                            font_test_list1 = [0, 0, 0]
                                        else:
                                            font_test_list1 = [255, 255, 255]
                                        font_test_list2.append(font_test_list1)
                                    font_test_list3.append(font_test_list2)
                                if font_test_list3 in localtion_spy_font.Num_pos_list:
                                    local_x_list.append(localtion_spy_font.Num_pos_wenzi_list[
                                                            localtion_spy_font.Num_pos_list.index(font_test_list3)])
                                else:
                                    break

                        # 检测 y字符
                        for local_pos in range(44, 55):
                            if local_pos_y_or_not is False:
                                local_pos_font = Image_array[51:61, local_pos:local_pos + 1]
                                for local_pos_font_element in local_pos_font:
                                    if np.array_equal(local_pos_font_element, np.array([[255, 255, 255]])):
                                        local_pos_y_or_not = True
                                        break
                                    else:
                                        pass
                            else:
                                break
                        else:
                            local_pos_wrong_mark = 1

                        local_pos = local_pos - 1
                        local_pos_font = Image_array[51:61, local_pos: local_pos + 7]

                        font_test_list3 = []
                        for font_array_2d in local_pos_font:
                            font_test_list2 = []
                            for font_array_1d in font_array_2d:
                                if not np.array_equal(font_array_1d, np.array([255, 255, 255])):
                                    font_test_list1 = [0, 0, 0]
                                else:
                                    font_test_list1 = [255, 255, 255]
                                font_test_list2.append(font_test_list1)
                            font_test_list3.append(font_test_list2)
                        if font_test_list3 == localtion_spy_font.P_y:
                            # 次数检测y坐标
                            local_pos = local_pos + 15
                            for local_pos in range(local_pos, local_pos + 24, 8):
                                if len(local_y_list) == 0:
                                    local_pos_font = Image_array[51:61, local_pos:local_pos + 8]
                                    font_test_list3 = []
                                    for font_array_2d in local_pos_font:
                                        font_test_list2 = []
                                        for font_array_1d in font_array_2d:
                                            if not np.array_equal(font_array_1d, np.array([255, 255, 255])):
                                                font_test_list1 = [0, 0, 0]
                                            else:
                                                font_test_list1 = [255, 255, 255]
                                            font_test_list2.append(font_test_list1)
                                        font_test_list3.append(font_test_list2)
                                    if font_test_list3 in localtion_spy_font.Num_pos_list:
                                        local_y_list.append(localtion_spy_font.Num_pos_wenzi_list[
                                                                localtion_spy_font.Num_pos_list.index(
                                                                    font_test_list3)])
                                    else:
                                        local_pos_wrong_mark = 1
                                        break
                                else:
                                    local_pos_font = Image_array[51:61, local_pos:local_pos + 8]
                                    font_test_list3 = []
                                    for font_array_2d in local_pos_font:
                                        font_test_list2 = []
                                        for font_array_1d in font_array_2d:
                                            if not np.array_equal(font_array_1d, np.array([255, 255, 255])):
                                                font_test_list1 = [0, 0, 0]
                                            else:
                                                font_test_list1 = [255, 255, 255]
                                            font_test_list2.append(font_test_list1)
                                        font_test_list3.append(font_test_list2)
                                    if font_test_list3 in localtion_spy_font.Num_pos_list:
                                        local_y_list.append(localtion_spy_font.Num_pos_wenzi_list[
                                                                localtion_spy_font.Num_pos_list.index(
                                                                    font_test_list3)])
                                    else:
                                        break
                        else:
                            local_pos_wrong_mark = 1
                        if local_pos_wrong_mark == 1:
                            local_x_list = [-1, -1, -1]
                            local_y_list = [-1, -1, -1]
                        else:
                            pass
                        raise SystemExit
                    else:
                        raise KeyboardInterrupt
        else:
            # 此时表示一直没有获取到颜色字体
            raise KeyboardInterrupt
    except KeyboardInterrupt:
        return 'cjcw'
        # print('场景错误')
    except SystemExit:
        local_x = sum([i * 10 ** index for index, i in enumerate(local_x_list[::-1])])
        local_y = sum([i * 10 ** index for index, i in enumerate(local_y_list[::-1])])
        # print(localtion_now, local_x, local_y)
        return [localtion_now, local_x, local_y]


if __name__ == '__main__':
    pass