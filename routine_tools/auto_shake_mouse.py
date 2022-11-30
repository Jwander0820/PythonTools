from time import time, sleep
from datetime import datetime
from pyautogui import moveRel, press, position


def avoid_screen_sleep():
    while True:
        mouse_pose = position()  # 取得並暫存當前滑鼠座標
        sleep(90)  # 休眠3分鐘(-5秒)後
        current_data_and_time = datetime.now()  # 取得當前時間
        current_time = current_data_and_time.strftime("%H:%M:%S")  # 顯示時間的格式
        current_time_int = current_data_and_time.strftime("%H%M%S")  # 用於計算的時間格式(int)
        print(f"{current_time}")
        if 120000 < int(current_time_int) < 130000:  # 若介於這段時間，不觸發搖晃功能
            print("_(:з」∠)_")
            print("午休啦別再搖了")
            continue
        if position() == mouse_pose:  # 再次取得滑鼠座標，若滑鼠座標相同，則觸發防止螢幕關閉的機制
            # 20221130；程式移動鼠標似乎還是無法阻止螢幕關閉，可以測試不同機器看有無差異
            # moveRel(0, 10, 1)  # 1秒內向下移動10pixel
            # moveRel(0, -10)
            press("capslock")  # 連續點擊兩次切換大小寫
            press("capslock")
            print("₍₍╰(*°▽°*)╯⁾⁾ ♪")
        else:
            print("_(´□`」∠)_")


if __name__ == "__main__":
    avoid_screen_sleep()
