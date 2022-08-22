import pynput
import time
import threading
import os
import redis
import json


board_controller = pynput.keyboard.Controller()
board_key = pynput.keyboard.Key
mouse_controller = pynput.mouse.Controller()
mouse_button = pynput.mouse.Button


def get_error():
    # os.system(cmd)
    while True:
        MH_Error_list = r.lrange('MH_Error', 0, -1)
        for MH_Error_item in MH_Error_list:
            MH_Error_dic = json.loads(MH_Error_item)
            for MH_Error_dic_item in MH_Error_dic:
                a, b, c = MH_Error_dic[MH_Error_dic_item]
                pingmu = pingmu_dic[MH_Error_dic_item]
                error_type = error_type_dic[c]
                print(pingmu + ' : ' + error_type)
            os.system(cmd)
        time.sleep(0.2)

def caozuo():
    while True:
        MH_Xiang_list = r.lrange('MH_Xiang', 0, -1)
        for MH_Xiang_item in MH_Xiang_list:
            MH_Xiang_dic = json.loads(MH_Xiang_item)
            for MH_Xiang_dic_item in MH_Xiang_dic:
                a, b = MH_Xiang_dic[MH_Xiang_dic_item]
                '''操作点香'''
                res = r.set(MH_Xiang_dic_item + '_smoke', 1, 1510)
            # 删除这个
            res = r.lrem('MH_Xiang', 0, MH_Xiang_item)
        MH_Task_list = r.lrange('MH_Task', 0, -1)
        time.sleep(0.1)

pid = os.getpid()
cmd = 'taskkill /pid ' + str(pid) + ' /f'
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.ltrim('MH_Error', -1, 0)
pingmu_dic = {'M1': '第一屏', 'M2': '第二屏', 'M3': '第三屏', 'M4': '第四屏'}
error_type_dic = {'1': '贼王异常', '2': '战斗异常', '3': '超数异常'}


if __name__ == '__main__':
    pass