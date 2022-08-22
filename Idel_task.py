from PIC import localtion_spy as l_spy
from PIC import task_spy as t_spy
import redis
import threading
import time
from PIL import ImageGrab
import numpy as np
import json


class Pingmu():
    def __init__(self, x, y, spot):
        self.x = x
        self.y = y
        self.spot = spot
        self.rw_step = 0
    def get_changjing(self):
        return l_spy.localtion_getter(self.x, self.y)
    def get_renwu(self):
        return t_spy.task_getter(self.x, self.y)
    def frightting_or_not(self):
        im = ImageGrab.grab((self.x+626, self.y+152, self.x+627, self.y+153))
        Image_array = np.array(im)
        if np.array_equal(Image_array, np.array([[[248, 248, 216]]])):
            return True
        else:
            return False
    def frightting_error_or_not(self):
        im = ImageGrab.grab((self.x, self.y + 204, self.x + 3, self.y + 476))
        Image_array = np.array(im)
        for Image_array_2d in Image_array:
            if np.array_equal(Image_array_2d, np.array([[248, 252, 248], [248, 252, 248], [248, 252, 248]])):
                return True
            else:
                return False

def people_status(MH):
    while True:
        if MH.rw_step == 1:
            # 判断是否在走动，若在走动，pass
            # 若没有走动，查询是否是在战斗状态，若在战斗状态，step=2，
            # 若是不是在战斗状态，判断MH_Task当中是否有该任务，若没有，添加，若有，pass
            MH_spot = 'S_' + MH.spot
            changjing_list = r.lrange(MH_spot, 0, -1)
            same_changjing = 0
            for changjing_item in changjing_list:
                if changjing_item == changjing_list[0]:
                    same_changjing += 1
                else:
                    pass

            if same_changjing > 5:
                if MH.frightting_or_not() is False:
                    MH_Task_list = r.lrange('MH_Task', 0, -1)
                    if str({MH.spot: (MH.x, MH.y)}) in MH_Task_list:
                        pass
                    else:
                        res = r.rpush('MH_Task', str({MH.spot: (MH.x, MH.y)}))
                else:
                    MH.rw_step = 2
            else:
                pass
        elif MH.rw_step == 2:
            # 查询异常池中是否有该错误（此时这里只捕捉是否贼王任务） M1:(x,y,异常类型) 1表示是贼王，后面2表示掉自动
            # 若有 pass
            # 若没有
                # 判断是否还在战斗状态，若还在战斗状态，pass 此时应该判断是否掉自动，但目前先不做
                # 若不是在战斗状态，判断是否是贼王任务。
                # 若是贼王任务，往异常池添加该错误，
                # 若为cw提示，则step=0，且向MH_Task添加该任务
                # 若返回的是列表，则step=1,
            rw_error_or_not = False
            MH_Error_list = r.lrange('MH_Error', 0, -1)
            for MH_Error_item in MH_Error_list:
                MH_Error_dic = json.loads(MH_Error_item)
                if MH.spot in MH_Error_dic.keys():
                    a, b, c = MH_Error_dic[MH.spot]
                    if c == 1 or c == 2:
                        rw_error_or_not = True
                        break
                    else:
                        pass
                else:
                    pass
            if rw_error_or_not is False:
                if MH.frightting_or_not() is False:
                    time.sleep(1.5)
                    MH_renwu = MH.get_renwu()
                    if MH_renwu == 'zw':
                        res = r.rpush('MH_Error', str({MH.spot: (MH.x, MH.y, 1)}))
                    # 此时手工去打贼王，有可能按地图时，这个任务会变成错误，但没关系
                    # 因为 此时已经把错误放在异常池，往后循环中，会直接pass
                    elif MH_renwu == 'cw':
                        MH.rw_step = 0
                        MH_time = r.get(MH.spot + '_time')
                        MH_time = int(MH_time) + 1
                        res = r.set(MH.spot + '_time', MH_time)
                        res = r.rpush('MH_Task', str({MH.spot: (MH.x, MH.y)}))
                    else:
                        MH_time = r.get(MH.spot + '_time')
                        MH_time = int(MH_time) + 1
                        res = r.set(MH.spot + '_time', MH_time)
                        MH.rw_step = 1
                # 在战斗中，判断是否战斗异常
                else:
                    if MH.frightting_error_or_not() is False:
                        pass
                    else:
                        # 战斗异常 可能是要点击人物，可能是掉了自动
                        res = r.rpush('MH_Error', str({MH.spot: (MH.x, MH.y, 2)}))
            else:
                pass
        else:
            renwu = MH.get_renwu()
            if isinstance(renwu, list):
                MH.rw_step = 1
            # 此时，若重启或第一次启动的情况，这个时候要告诉操作端，可以操作了
            else:
                MH_Task_list = r.lrange('MH_Task', 0, -1)
                for MH_Task_item in MH_Task_list:
                    if MH.spot in json.loads(MH_Task_item).keys():
                        pass
                    else:
                        res = r.rpush('MH_Task', str({MH.spot: (MH.x, MH.y)}))
                        break
        time.sleep(0.5)

def changjing_gen(MH):
    while True:
        changjing = MH.get_changjing()
        if changjing != 'cjcw':
            MH_spot = 'S_' + MH.spot
            r.lpush(MH_spot, str({changjing[0]: (changjing[1], changjing[2])}))
        else:
            pass
        time.sleep(0.5)

def changjing_trim(MH):
    while True:
        MH_spot = 'S_' + MH.spot
        res = r.ltrim(MH_spot, 0, 20)
        time.sleep(6)
# 设置香
def set_xiang(MH):
    while True:
        MH_spot = MH.spot
        if r.get(MH_spot + '_smoke') is None:
            MH_Xiang_list = r.lrange('MH_Xiang', 0, -1)
            for MH_Xiang_item in MH_Xiang_list:
                if MH.spot in json.loads(MH_Xiang_item).keys():
                    pass
                else:
                    res = r.rpush('MH_Xiang', str({MH_spot: (MH.x, MH.y)}))
        else:
            pass
        time.sleep(30)

def calcu_time(MH):
    while True:
        if int(r.get(MH.spot + '_time')) > 200:
            MH_Error_list = r.lrange('MH_Error', 0, -1)
            for MH_Error_item in MH_Error_list:
                MH_Error_dic = json.loads(MH_Error_item)
                if MH.spot in MH_Error_dic.keys():
                    a, b, c = MH_Error_dic[MH.spot]
                    if c == 3:
                        pass
                    else:
                        res = r.rpush('MH_Error', str({MH.spot: (MH.x, MH.y, 3)}))
                else:
                    pass
        else:
            pass
        time.sleep(5)

if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    MH1 = Pingmu(20, 16, 'M1')
    # MH2 = Pingmu(664, 6, 'M2')
    # MH3 = Pingmu(9, 526, 'M3')
    # MH_list = [MH1, MH2, MH3]
    MH_list = [MH1]
    for MH in MH_list:
        threading.Thread(target=people_status, args=(MH,)).start()
        threading.Thread(target=changjing_gen, args=(MH,)).start()
        threading.Thread(target=changjing_trim, args=(MH,)).start()
        threading.Thread(target=set_xiang, args=(MH,)).start()
        threading.Thread(target=calcu_time, args=(MH,)).start()
