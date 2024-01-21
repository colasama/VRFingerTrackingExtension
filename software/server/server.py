from rich.console import Console
from rich.progress import track, Progress
import time
import serial
import random
# from libs.kalman_filter import KalmanFilter
# import numpy as np


ser = serial.Serial('COM4',115200,timeout=5)
VERSION = "0.0.1"
CALI_TIMES = 100
fingers_max = [100] * 10
fingers_min = [0] * 10
fingers_values = [0] * 10
fingers_tasks = []
fingers_ports = [4]
# Init rich console
console = Console()
# def change_value(progress, task):
    # progress.update(task, advance= ,)


# Calibrate the max value of touch sensor
def cali_max_touch_value(id):
    global fingers_max
    temp = 0
    console.log("正在校准 ID 为 " + str(id) + " 位于端口 " + str(fingers_ports[id]) + " 的手指传感器...")
    i = 0
    while i < CALI_TIMES:
        target = ser.readline().decode()
        if "Filt" in target:
            temp = temp + float(target.split(" ")[1].strip('\t\r\n').split("\t")[fingers_ports[id]])
            i = i + 1
            time.sleep(0.01)
    temp = temp / CALI_TIMES
    console.log(temp)
    fingers_max[id] = temp
    console.log("校准完毕！")


def get_value_from_serial(id):
    global fingers_values
    target = ser.readline().decode()
    if "Filt" in target:
        touch_value = float(target.split(" ")[1].strip('\t\r\n').split("\t")[fingers_ports[id]])
        res = touch_value - fingers_values[id]
        fingers_values[id] = touch_value
        return res
    else:
        return 0

if __name__ == "__main__":
    # while True:
    #     target = ser.readline().decode()
    #     if "Filt" in target:
    #         target_list = target.split(" ")[1].strip('\t\r\n').split("\t")
            # console.log(target_list[2])
    
    with Progress() as progress:
        for i in range(1):
            cali_max_touch_value(i)
            temp_task = progress.add_task("Finger " + str(i), total=fingers_max[i] * 1.05)
            fingers_tasks.append(temp_task)

        while(True):
            # print(get_value_from_serial(4))
            # continue
            for i in range(1):
                # progress.update(fingers_tasks[i], advance=get_value_from_serial(i))
                progress.update(fingers_tasks[i], advance=get_value_from_serial(i))
                # time.sleep(0.02)
        # while not progress.finished: