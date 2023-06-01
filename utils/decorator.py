import threading
import time
from functools import wraps


def debounce(wait):
    """
    裝飾器，將函數的執行延遲到從上一次調用開始經過 wait 秒後
    當你呼叫一個函數時，它不會立即執行，而是等待一段時間(wait秒)
    如果在等待期間再次呼叫該函數，那麼前一次的呼叫就會被取消，並重新開始計時。等到沒有新的呼叫時，最後一次的呼叫將會被執行。
    :param wait: 要延遲的時間，單位為秒
    :return:
    """

    def decorator(fn):
        """
        裝飾器本身，會裝飾被傳入的函數 fn
        :param fn:要被裝飾的函數
        :return:
        """
        timer = None

        @wraps(fn)
        def debounced(*args, **kwargs):
            """
            裝飾過後的函數。當它被調用時，會延遲 wait 秒再真正執行。
            :param args:被裝飾的函數的參數
            :param kwargs:被裝飾的函數的參數
            :return:
            """
            nonlocal timer

            def call_it():
                """實際調用函數的內部函數"""
                fn(*args, **kwargs)

            # 如果已經有一個計時器在運行（也就是說函數已經被調用過但還沒有執行），那就取消它
            if timer is not None:
                timer.cancel()

            # 建立一個新的計時器，wait 秒後調用函數
            timer = threading.Timer(wait, call_it)
            timer.start()

        return debounced

    return decorator


def timer(func):
    """
    計時器，紀錄函數執行時間
    :param func: 函數
    :return:
    """

    def inner(*args, **kwargs):
        start_time = time.time()  # 紀錄起始時間
        try:
            res = func(*args, **kwargs)  # 執行函數
            end_time = time.time()  # 紀錄結束時間
            print(f"time consume {sec2sec(start_time, end_time)} sec.")
            return res
        except Exception as e:
            end_time = time.time()
            print(f"time consume {sec2sec(start_time, end_time)} sec.")

    return inner


def sec2sec(start_time, end_time, decimal_places=2):
    """
    將計時器的總秒數轉換成 x 秒
    :param start_time:計時器開始的時間
    :param end_time:計時器結束的時間
    :param decimal_places:要呈現多少位小數點
    :return:
    """
    calculating_time_sec = round(end_time - start_time, decimal_places)
    return calculating_time_sec


class TestDecorator:

    @debounce(0.2)
    def test_func(self):
        print("call test_func")

    def test_debounce(self):
        for i in range(10):
            self.test_func()
            time.sleep(0.3)
        print("---")
        for i in range(10):
            self.test_func()
            time.sleep(0.1)

    @timer
    def test_timer(self):
        time.sleep(1)


if __name__ == '__main__':
    TestDecorator().test_debounce()
    TestDecorator().test_timer()
