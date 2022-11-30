from time import time, sleep
from datetime import datetime
from pyautogui import moveRel


def avoid_screen_sleep():
    while True:
        sleep(177)  # 休眠3分鐘(-3秒)後
        current_data_and_time = datetime.now()  # 取得當前時間
        current_time = current_data_and_time.strftime("%H:%M:%S")  # 顯示時間的格式
        current_time_int = current_data_and_time.strftime("%H%M%S")  # 用於計算的時間格式(int)
        print(f"{current_time}")
        if 120000 < int(current_time_int) < 130000:  # 若介於這段時間，不觸發搖晃功能
            print("_(:з」∠)_")
            print("午休啦別再搖了")
            continue
        moveRel(0, 1)  # 向下移動1pixel
        print("₍₍╰(*°▽°*)╯⁾⁾ ♪")


if __name__ == "__main__":
    avoid_screen_sleep()
