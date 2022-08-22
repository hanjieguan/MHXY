from PIL import ImageGrab
import numpy as np
import task_spy_font


def task_getter(pos_original_x, pos_original_y):
    # 489 174 挖
    pos_wa_x = pos_original_x + 483
    pos_wa_y = pos_original_y + 174
    pos_wa_x2 = pos_wa_x + 140
    pos_wa_y2 = pos_wa_y + 85
    im = ImageGrab.grab((pos_wa_x, pos_wa_y, pos_wa_x2, pos_wa_y2))
    Image_array = np.array(im)
    # 挖字位置
    font_test = Image_array[0:7, 0:13]
    font_test_list3 = []
    for font_test_2d in font_test:
        font_test_list2 = []
        for font_test_1d in font_test_2d:
            if np.array_equal(font_test_1d, np.array([0, 255, 0])):
                font_test_list1 = [0, 255, 0]
            else:
                font_test_list1 = [0, 0, 0]
            font_test_list2.append(font_test_list1)
        font_test_list3.append(font_test_list2)
    # 是否是‘挖’字
    if font_test_list3 == task_spy_font.WA_half:
        # 设置红色次数
        redword_time = 0
        # 初始字体颜色 白色
        # orginal_font_color = 0
        # 当前字体颜色
        now_font_color = 0
        # print('true')
        # 最终想要获取的数据如下：
        # 挖宝类型 普通挖宝，贼王挖宝，默认普通挖宝
        wb_type = None
        # 挖宝场景
        wb_place = None
        # 挖宝坐标
        # wb_x = None
        # wb_y = None
        # 坐标列表
        coor_x_list = []
        coor_y_list = []
        try:
            # 总共五行 任务信息
            for readrows in range(1, 6):
                # 检测第一行，全部为中文，9-10个字
                if readrows == 1:
                    for font_columns in range(14, 127, 14):
                        # 设置 进入单字时 默认标识为空
                        single_font_signal = 0
                        # 设置 进入单字时，把当前获取到的颜色赋予原始(前一个)颜色
                        orginal_font_color = now_font_color
                        # 单个字的列数，节省时间只检查到第3列
                        for font_single_columns in range(0, 3):
                            if single_font_signal == 1:
                                break
                            else:
                                now_font_tictlk = Image_array[15:29,
                                                  font_columns + font_single_columns:font_columns + font_single_columns + 1]
                                for now_font_tictlk_element in now_font_tictlk:
                                    if single_font_signal == 1:
                                        break
                                    else:
                                        if np.array_equal(now_font_tictlk_element, np.array([[255, 255, 255]])):
                                            # 白色
                                            single_font_signal = 1
                                            now_font_color = 0
                                        elif np.array_equal(now_font_tictlk_element, np.array([[255, 0, 0]])):
                                            # 红色
                                            single_font_signal = 1
                                            now_font_color = 1
                                        else:
                                            # 没有颜色 无文字
                                            pass
                        if orginal_font_color != now_font_color:
                            # 由白转红
                            if now_font_color == 1:
                                redword_time += 1
                                # 获得红字
                                # 先得到该单字前面六个像素的数组
                                font_test = Image_array[15:29, font_columns:font_columns + 6]
                                font_test_list3 = []
                                for font_test_2d in font_test:
                                    font_test_list2 = []
                                    for font_test_1d in font_test_2d:
                                        if np.array_equal(font_test_1d, np.array([255, 0, 0])):
                                            font_test_list1 = [255, 0, 0]
                                        else:
                                            font_test_list1 = [0, 0, 0]
                                        font_test_list2.append(font_test_list1)
                                    font_test_list3.append(font_test_list2)
                                # 在此去比较红字信息
                                if redword_time == 1:
                                    # 此时的font_test_list3 为获取单字六个像素的结果，再与之比较
                                    # 先判断是否为 强 字，再判断是否是地名，若都不是，则直接返回贼王任务
                                    if font_test_list3 == task_spy_font.RED_qiang:
                                        # 此时表示为普通挖宝任务，已经默认任务类型为0
                                        wb_type = 0
                                    elif font_test_list3 in task_spy_font.Local_list:
                                        # 此时找出 挖宝场景
                                        wb_place = task_spy_font.Local_wenzi_list[
                                            task_spy_font.Local_list.index(font_test_list3)]
                                    else:
                                        raise KeyboardInterrupt
                                # 第一行红字最多出现两次，所以else为第二次，因为肯定大于0,且不可能为数字
                                else:
                                    # 判断是否为 强 字，若为 强 字，则由第一个红字场景过来的；再判断 是否在 场景列表，若在场景列表，则由第一个红字强盗过来的；否则为贼王
                                    if font_test_list3 == task_spy_font.RED_qiang:
                                        # 此时表示为普通挖宝任务，已经默认任务类型为0
                                        wb_type = 0
                                    elif font_test_list3 in task_spy_font.Local_list:
                                        # 此时找出 挖宝场景
                                        wb_place = task_spy_font.Local_wenzi_list[
                                            task_spy_font.Local_list.index(font_test_list3)]
                                    else:
                                        raise KeyboardInterrupt
                            # 由红转白，忽略
                            else:
                                pass
                        # 颜色相同，忽略
                        else:
                            pass
                # 其他行数
                else:
                    # 红色逗号只有一个
                    red_comma = 0
                    # 由白转红时，第一个文字类型
                    red_font_type = 0
                    # 由第一行检测出来，只有一条信息的，说明红字=1
                    # 第一行检测出来场景，此时，还有可能是贼王任务，或普通任务
                    if wb_type is None and wb_place is not None:
                        for font_rows in range(29, 86, 14):
                            # 初始列数
                            orginal_column = 0
                            while orginal_column < 138:
                                # 设置 进入单字时，把当前获取到的颜色赋予原始(前一个)颜色
                                orginal_font_color = now_font_color
                                # 设置 进入单字时 默认标识为空 用于获取到颜色后退出
                                single_font_signal = 0
                                # 设置 进入单字时 遇到无颜色的情况标识
                                single_font_none_signal = 0
                                for font_single_columns in range(0, 3):
                                    if single_font_signal == 1:
                                        break
                                    else:
                                        now_font_tictlk = Image_array[font_rows:font_rows + 14,
                                                          orginal_column + font_single_columns:orginal_column + font_single_columns + 1]
                                        for now_font_tictlk_element in now_font_tictlk:
                                            if single_font_signal == 1:
                                                break
                                            else:
                                                if np.array_equal(now_font_tictlk_element, np.array([[255, 255, 255]])):
                                                    # 白色
                                                    single_font_signal = 1
                                                    now_font_color = 0
                                                elif np.array_equal(now_font_tictlk_element, np.array([[255, 0, 0]])):
                                                    # 红色
                                                    single_font_signal = 1
                                                    now_font_color = 1
                                                else:
                                                    # 没有颜色 无文字
                                                    single_font_none_signal = 1
                                # 记录红色次数
                                if orginal_font_color != now_font_color:
                                    # 由白转红
                                    if now_font_color == 1:
                                        redword_time += 1
                                        # 获取红字里面第一个字的信息
                                        font_test = Image_array[font_rows:font_rows + 14,
                                                    orginal_column:orginal_column + 6]
                                        font_test_list3 = []
                                        for font_test_2d in font_test:
                                            font_test_list2 = []
                                            for font_test_1d in font_test_2d:
                                                if np.array_equal(font_test_1d, np.array([255, 0, 0])):
                                                    font_test_list1 = [255, 0, 0]
                                                else:
                                                    font_test_list1 = [0, 0, 0]
                                                font_test_list2.append(font_test_list1)
                                            font_test_list3.append(font_test_list2)
                                        # 普通任务，强盗
                                        if font_test_list3 == task_spy_font.RED_qiang:
                                            red_font_type = 1
                                        # 为红色数字
                                        elif font_test_list3 in task_spy_font.Num_list:
                                            red_font_type = 2
                                        # 贼王任务
                                        else:
                                            raise KeyboardInterrupt
                                    # 由红转白
                                    else:
                                        pass
                                # 颜色一样
                                else:
                                    pass

                                # 判读
                                if redword_time == 1:
                                    # 当前字体颜色仍为白色，或者若为无色，加上14以后，也是比138大，可以退出循环，
                                    # 仍是第一次红色的情况，一般只出现在第二行
                                    orginal_column = orginal_column + 14
                                elif redword_time == 2:
                                    if single_font_none_signal != 0:
                                        if now_font_color == 0:
                                            orginal_column = orginal_column + 14
                                        # 当前为红字
                                        else:
                                            # 此时的红字，只可能是普通任务，且未获取坐标
                                            if red_font_type == 1:
                                                orginal_column = orginal_column + 14
                                            # 此时的红字为数字，即坐标
                                            else:
                                                # 获取当前数字信息
                                                font_test = Image_array[font_rows:font_rows + 14,
                                                            orginal_column:orginal_column + 6]
                                                font_test_list3 = []
                                                for font_test_2d in font_test:
                                                    font_test_list2 = []
                                                    for font_test_1d in font_test_2d:
                                                        if np.array_equal(font_test_1d, np.array([255, 0, 0])):
                                                            font_test_list1 = [255, 0, 0]
                                                        else:
                                                            font_test_list1 = [0, 0, 0]
                                                        font_test_list2.append(font_test_list1)
                                                    font_test_list3.append(font_test_list2)
                                                if font_test_list3 in task_spy_font.Num_list:
                                                    font_test = task_spy_font.Num_num_list[
                                                        task_spy_font.Num_list.index(font_test_list3)]
                                                    if red_comma == 0:
                                                        coor_x_list.append(font_test)
                                                    else:
                                                        coor_y_list.append(font_test)
                                                    orginal_column = orginal_column + 7
                                                else:
                                                    red_comma = 1
                                                    orginal_column = orginal_column + 14
                                    else:
                                        orginal_column = orginal_column + 14
                                else:
                                    if single_font_none_signal != 0:
                                        if now_font_color == 0:
                                            raise Exception
                                        else:
                                            # 此时的红字，只可能是普通任务，第三次出现红字，且未出现贼王信息，此时可以直接返回普通任务
                                            if red_font_type == 1:
                                                raise Exception
                                            # 此时的红字为数字，即坐标，第三次才出现坐标，且未普通任务，挨个获取坐标信息
                                            else:
                                                # 获取当前数字信息
                                                font_test = Image_array[font_rows:font_rows + 14,
                                                            orginal_column:orginal_column + 6]
                                                font_test_list3 = []
                                                for font_test_2d in font_test:
                                                    font_test_list2 = []
                                                    for font_test_1d in font_test_2d:
                                                        if np.array_equal(font_test_1d, np.array([255, 0, 0])):
                                                            font_test_list1 = [255, 0, 0]
                                                        else:
                                                            font_test_list1 = [0, 0, 0]
                                                        font_test_list2.append(font_test_list1)
                                                    font_test_list3.append(font_test_list2)
                                                if font_test_list3 in task_spy_font.Num_list:
                                                    font_test = task_spy_font.Num_num_list[
                                                        task_spy_font.Num_list.index(font_test_list3)]
                                                    if red_comma == 0:
                                                        coor_x_list.append(font_test)
                                                    else:
                                                        coor_y_list.append(font_test)
                                                    orginal_column = orginal_column + 7
                                                else:
                                                    red_comma = 1
                                                    orginal_column = orginal_column + 14
                                    else:
                                        orginal_column = orginal_column + 14
                    # 由第一行检测出来的任务类型，只能是普通挖宝任务，接下来要么地点，要么坐标
                    elif wb_place is None and wb_type is not None:
                        for font_rows in range(29, 86, 14):
                            # 初始列数
                            orginal_column = 0
                            while orginal_column < 138:
                                # 设置 进入单字时，把当前获取到的颜色赋予原始(前一个)颜色
                                orginal_font_color = now_font_color
                                # 设置 进入单字时 默认标识为空 用于获取到颜色后退出
                                single_font_signal = 0
                                # 设置 进入单字时 遇到无颜色的情况标识
                                single_font_none_signal = 0
                                for font_single_columns in range(0, 3):
                                    if single_font_signal == 1:
                                        break
                                    else:
                                        now_font_tictlk = Image_array[font_rows:font_rows + 14,
                                                          orginal_column + font_single_columns:orginal_column + font_single_columns + 1]
                                        for now_font_tictlk_element in now_font_tictlk:
                                            if single_font_signal == 1:
                                                break
                                            else:
                                                if np.array_equal(now_font_tictlk_element, np.array([[255, 255, 255]])):
                                                    # 白色
                                                    single_font_signal = 1
                                                    now_font_color = 0
                                                elif np.array_equal(now_font_tictlk_element, np.array([[255, 0, 0]])):
                                                    # 红色
                                                    single_font_signal = 1
                                                    now_font_color = 1
                                                else:
                                                    # 没有颜色 无文字
                                                    single_font_none_signal = 1
                                # 记录红色次数
                                if orginal_font_color != now_font_color:
                                    # 由白转红
                                    if now_font_color == 1:
                                        redword_time += 1
                                        # 获取红字里面第一个字的信息
                                        font_test = Image_array[font_rows:font_rows + 14,
                                                    orginal_column:orginal_column + 6]
                                        font_test_list3 = []
                                        for font_test_2d in font_test:
                                            font_test_list2 = []
                                            for font_test_1d in font_test_2d:
                                                if np.array_equal(font_test_1d, np.array([255, 0, 0])):
                                                    font_test_list1 = [255, 0, 0]
                                                else:
                                                    font_test_list1 = [0, 0, 0]
                                                font_test_list2.append(font_test_list1)
                                            font_test_list3.append(font_test_list2)
                                            # 若为场景
                                            if font_test_list3 in task_spy_font.Local_list:
                                                red_font_type = 1
                                                wb_place = task_spy_font.Local_wenzi_list[
                                                    task_spy_font.Local_list.index(font_test_list3)]
                                            # 否则则为坐标位置
                                            else:
                                                red_font_type = 2
                                    # 由红转白
                                    else:
                                        pass
                                # 颜色一样
                                else:
                                    pass
                                # 判读
                                if redword_time == 1:
                                    # 当前字体颜色仍为白色，或者若为无色，加上14以后，也是比138大，可以退出循环，
                                    # 仍是第一次红色的情况，一般只出现在第二行
                                    orginal_column = orginal_column + 14
                                elif redword_time == 2:
                                    if single_font_none_signal != 0:
                                        if now_font_color == 0:
                                            orginal_column = orginal_column + 14
                                        # 当前为红字
                                        else:
                                            # 此时的红字，只可能是普通任务，且当前情况只能是场景。且未获取坐标
                                            if red_font_type == 1:
                                                orginal_column = orginal_column + 14
                                            # 此时的红字为数字，即坐标
                                            else:
                                                # 获取当前数字信息
                                                font_test = Image_array[font_rows:font_rows + 14,
                                                            orginal_column:orginal_column + 6]
                                                font_test_list3 = []
                                                for font_test_2d in font_test:
                                                    font_test_list2 = []
                                                    for font_test_1d in font_test_2d:
                                                        if np.array_equal(font_test_1d, np.array([255, 0, 0])):
                                                            font_test_list1 = [255, 0, 0]
                                                        else:
                                                            font_test_list1 = [0, 0, 0]
                                                        font_test_list2.append(font_test_list1)
                                                    font_test_list3.append(font_test_list2)
                                                if font_test_list3 in task_spy_font.Num_list:
                                                    font_test = task_spy_font.Num_num_list[
                                                        task_spy_font.Num_list.index(font_test_list3)]
                                                    if red_comma == 0:
                                                        coor_x_list.append(font_test)
                                                    else:
                                                        coor_y_list.append(font_test)
                                                    orginal_column = orginal_column + 7
                                                else:
                                                    red_comma = 1
                                                    orginal_column = orginal_column + 14
                                    else:
                                        orginal_column = orginal_column + 14
                                # 表示第三次出现红字,但坐标可能还没有获取完
                                else:
                                    if single_font_none_signal != 0:
                                        if now_font_color == 0:
                                            raise Exception
                                        else:
                                            # 此时的红字，只可能是普通任务，第三次出现红字，坐标在第二次已经获取完，且第三次记录红字时，已经获取了场景，可以直接返回
                                            if red_font_type == 1:
                                                raise Exception
                                            # 此时的红字为数字，即坐标，第三次才出现坐标，且未普通任务，挨个获取坐标信息
                                            else:
                                                # 获取当前数字信息
                                                font_test = Image_array[font_rows:font_rows + 14,
                                                            orginal_column:orginal_column + 6]
                                                font_test_list3 = []
                                                for font_test_2d in font_test:
                                                    font_test_list2 = []
                                                    for font_test_1d in font_test_2d:
                                                        if np.array_equal(font_test_1d, np.array([255, 0, 0])):
                                                            font_test_list1 = [255, 0, 0]
                                                        else:
                                                            font_test_list1 = [0, 0, 0]
                                                        font_test_list2.append(font_test_list1)
                                                    font_test_list3.append(font_test_list2)
                                                if font_test_list3 in task_spy_font.Num_list:
                                                    font_test = task_spy_font.Num_num_list[
                                                        task_spy_font.Num_list.index(font_test_list3)]
                                                    if red_comma == 0:
                                                        coor_x_list.append(font_test)
                                                    else:
                                                        coor_y_list.append(font_test)
                                                    orginal_column = orginal_column + 7
                                                else:
                                                    red_comma = 1
                                                    orginal_column = orginal_column + 14
                                    else:
                                        orginal_column = orginal_column + 14
                    # 此时红字=2
                    # 第一行肯定会包含一种类型，所以else表示 任务类型和任务场景都不为空的情况
                    # 此时只剩下坐标需要检测，且肯定为普通挖宝任务
                    # 这种可能只有 据XX反映，强盗。。。
                    else:
                        for font_rows in range(29, 86, 14):
                            # 初始列数
                            orginal_column = 0
                            while orginal_column < 138:
                                # 设置 进入单字时，把当前获取到的颜色赋予原始(前一个)颜色
                                orginal_font_color = now_font_color
                                # 设置 进入单字时 默认标识为空 用于获取到颜色后退出
                                single_font_signal = 0
                                # 设置 进入单字时 遇到无颜色的情况标识
                                single_font_none_signal = 0
                                for font_single_columns in range(0, 3):
                                    if single_font_signal == 1:
                                        break
                                    else:
                                        now_font_tictlk = Image_array[font_rows:font_rows + 14,
                                                          orginal_column + font_single_columns:orginal_column + font_single_columns + 1]
                                        for now_font_tictlk_element in now_font_tictlk:
                                            if single_font_signal == 1:
                                                break
                                            else:
                                                if np.array_equal(now_font_tictlk_element, np.array([[255, 255, 255]])):
                                                    # 白色
                                                    single_font_signal = 1
                                                    now_font_color = 0
                                                elif np.array_equal(now_font_tictlk_element, np.array([[255, 0, 0]])):
                                                    # 红色
                                                    single_font_signal = 1
                                                    now_font_color = 1
                                                else:
                                                    # 没有颜色 无文字
                                                    single_font_none_signal = 1
                                # 记录红色次数
                                if orginal_font_color != now_font_color:
                                    # 由白转红
                                    if now_font_color == 1:
                                        redword_time += 1
                                    # 由红转白
                                    else:
                                        pass
                                # 颜色一样
                                else:
                                    pass

                                # 判读
                                # 若红字还是第二次，则当前认为白色，或无色
                                if redword_time == 2:
                                    orginal_column = orginal_column + 14
                                else:
                                    if single_font_none_signal != 0:
                                        if now_font_color == 0:
                                            raise Exception
                                        else:
                                            # 此时的红字为数字，即坐标，第三次才出现坐标，且未普通任务，挨个获取坐标信息
                                            # 获取当前数字信息
                                            font_test = Image_array[font_rows:font_rows + 14,
                                                        orginal_column:orginal_column + 6]
                                            font_test_list3 = []
                                            for font_test_2d in font_test:
                                                font_test_list2 = []
                                                for font_test_1d in font_test_2d:
                                                    if np.array_equal(font_test_1d, np.array([255, 0, 0])):
                                                        font_test_list1 = [255, 0, 0]
                                                    else:
                                                        font_test_list1 = [0, 0, 0]
                                                    font_test_list2.append(font_test_list1)
                                                font_test_list3.append(font_test_list2)
                                            if font_test_list3 in task_spy_font.Num_list:
                                                font_test = task_spy_font.Num_num_list[
                                                    task_spy_font.Num_list.index(font_test_list3)]
                                                if red_comma == 0:
                                                    coor_x_list.append(font_test)
                                                else:
                                                    coor_y_list.append(font_test)
                                                orginal_column = orginal_column + 7
                                            else:
                                                red_comma = 1
                                                orginal_column = orginal_column + 14
                                    else:
                                        orginal_column = orginal_column + 14

        # 抛出异常 告诉是贼王任务
        except KeyboardInterrupt:
            return 'zw'
        # 抛出异常，完结普通任务
        except Exception:
            coor_x_list = [i * 10 ** index for index, i in enumerate(coor_x_list[::-1])]
            wb_x = sum(coor_x_list)
            coor_y_list = [i * 10 ** index for index, i in enumerate(coor_y_list[::-1])]
            wb_y = sum(coor_y_list)
            return [wb_place, wb_x, wb_y]
            # print('普通任务', wb_place, wb_x, wb_y)
        # 保持try完整性，没有实际意义
        else:
            pass
    # 此时抛出异常 让程序终止
    else:
        return 'cw'


if __name__ == '__main__':
    pass