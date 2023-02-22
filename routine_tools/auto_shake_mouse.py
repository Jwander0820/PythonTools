import logging
import os
import sys
import time
from datetime import datetime
from logging.handlers import RotatingFileHandler
from time import sleep

from pyautogui import press, position

# 設定log handler
LOG_FILE_NAME = 'avoid_screen_sleep.log'
LOG_MAX_BYTES = 500000  # 500KB
LOG_BACKUP_COUNT = 1  # 保留最近的1個log檔案
handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=LOG_MAX_BYTES, backupCount=LOG_BACKUP_COUNT)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger = logging.getLogger(LOG_FILE_NAME)
logger.setLevel('DEBUG')
logger.addHandler(handler)


def avoid_screen_sleep():
    shake = True  # 開關設定
    while shake:
        try:
            mouse_pose = position()  # 取得並暫存當前滑鼠座標
            sleep(90)  # 休眠時間為3分鐘，須設定為休眠時間的一半
            current_data_and_time = datetime.now()  # 取得當前時間
            current_time = current_data_and_time.strftime("%H:%M:%S")  # 顯示時間的格式
            current_time_int = current_data_and_time.strftime("%H%M%S")  # 用於計算的時間格式(int)
            # 檢測是否於指定時段，觸發相對應的功能
            if 120000 < int(current_time_int) < 130000:  # 若介於這段時間，不觸發防止螢幕關閉的機制
                print(f"{current_time} 休息中 _(:з」∠)_")
                logger.info("休息中")  # 累了...想睡...
                continue
            elif int(current_time_int) > 173000:  # 若時間超過17:30，自動關閉程式
                print(f"{current_time} 戰略性撤退 (((┏ (;￣▽￣)┛")  # 塊陶R
                print(f"{current_time} 下班啦~程式也要閃人啦~8888~")
                logger.info("戰略性撤退")
                logger.info("下班啦~程式也要閃人啦~8888~")
                sleep(10)  # 休息10秒，喘一下
                shake = False  # 停止迴圈，關閉程式
                continue

            # 再次取得滑鼠座標，若滑鼠座標相同，則觸發防止螢幕關閉的機制
            if position() == mouse_pose:
                press("capslock")  # 連續點擊兩次切換大小寫
                press("capslock")
                print(f"{current_time} 搖起來 ₍₍╰(*°▽°*)╯⁾⁾ ♪")
                logger.info("搖起來")  # 啟動防止螢幕關閉時顯示該符號
            else:
                print(f"{current_time} 好累喔 _(´□`」∠)_")
                logger.info("好累喔")  # 未啟動防止螢幕關閉時顯示該符號

        except Exception as e:
            logger.info("錯誤啦")
            logger.info(e, exc_info=True)
            time.sleep(5)
            # 使用os.execv重新啟動程式
            # 注意：sys.argv[0]是指當前的.py或.exe檔案名稱
            os.execv(sys.executable, ['python'] + sys.argv)


if __name__ == "__main__":
    avoid_screen_sleep()
