from time import time, sleep
from datetime import datetime
from pyautogui import moveRel, press, position


def avoid_screen_sleep():
    shake = True  # 開關設定
    while shake:
        mouse_pose = position()  # 取得並暫存當前滑鼠座標
        sleep(90)  # 休眠時間為3分鐘，須設定為休眠時間的一半
        current_data_and_time = datetime.now()  # 取得當前時間
        current_time = current_data_and_time.strftime("%H:%M:%S")  # 顯示時間的格式
        current_time_int = current_data_and_time.strftime("%H%M%S")  # 用於計算的時間格式(int)
        print(f"{current_time}")
        # 檢測是否於指定時段，觸發相對應的功能
        if 120000 < int(current_time_int) < 130000:  # 若介於這段時間，不觸發防止螢幕關閉的機制
            print("_(:з」∠)_")  # 累了...想睡...
            continue
        elif int(current_time_int) > 173000:  # 若時間超過17:30，自動關閉程式
            print("(((┏ (;￣▽￣)┛")  # 塊陶R
            print("下班啦~程式也要閃人啦~8888~")
            sleep(10)  # 休息10秒，喘一下
            shake = False  # 停止迴圈，關閉程式
            continue

        # 再次取得滑鼠座標，若滑鼠座標相同，則觸發防止螢幕關閉的機制
        if position() == mouse_pose:
            # 20221130；程式移動鼠標似乎還是無法阻止螢幕關閉，可以測試不同機器看有無差異
            # moveRel(0, 10, 1)  # 1秒內向下移動10pixel
            # moveRel(0, -10)
            press("capslock")  # 連續點擊兩次切換大小寫
            press("capslock")
            print("₍₍╰(*°▽°*)╯⁾⁾ ♪")  # 啟動防止螢幕關閉時顯示該符號
        else:
            print("_(´□`」∠)_")  # 未啟動防止螢幕關閉時顯示該符號


if __name__ == "__main__":
    avoid_screen_sleep()
