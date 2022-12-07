from pyautogui import keyDown, keyUp, press


class FuncKey:
    @staticmethod
    def ctrl_c():
        """
        ctrl + c : 複製
        :return:
        """
        keyDown('ctrl')
        press('c')
        keyUp('ctrl')

    @staticmethod
    def ctrl_v_enter():
        """
        ctrl+ v + enter : 貼上 + Enter
        :return:
        """
        keyDown('ctrl')
        press('v')
        keyUp('ctrl')
        press('enter')

    @staticmethod
    def ctrl_a():
        """
        ctrl + a : 全選
        :return:
        """
        keyDown('ctrl')
        press('a')
        keyUp('ctrl')

    @staticmethod
    def alt_tab():
        """
        alt + tab : 切換視窗
        :return:
        """
        keyDown('alt')
        press('tab')
        keyUp('alt')

    @staticmethod
    def ctrl_win_left():
        """
        ctrl + win + left : 向左切換桌面
        :return:
        """
        keyDown('ctrl')
        keyDown('win')
        press('left')
        keyUp('ctrl')
        keyUp('win')

    @staticmethod
    def ctrl_win_right():
        """
        ctrl + win + right : 向右切換桌面
        :return:
        """
        keyDown('ctrl')
        keyDown('win')
        press('right')
        keyUp('ctrl')
        keyUp('win')

    @staticmethod
    def right_click():
        """
        shift + f10 : 鍵盤模擬滑鼠點擊右鍵的選單功能
        :return:
        """
        keyDown('shift')
        press('f10')
        keyUp('shift')

    @staticmethod
    def enter():
        """
        enter : 輸入使用
        :return:
        """
        press('enter')

    @staticmethod
    def left():
        """
        left : 方向左鍵
        :return:
        """
        press('left')

    @staticmethod
    def right():
        """
        right : 方向右鍵
        :return:
        """
        press('right')

    @staticmethod
    def up():
        """
        up : 方向上鍵
        :return:
        """
        press('up')

    @staticmethod
    def down():
        """
        down : 方向下鍵
        :return: 
        """
        press('down')

    @staticmethod
    def win_h():
        """
        win + h : 呼叫windows快捷鍵，windows語音輸入功能
        :return:
        """
        keyDown('win')
        press('h')
        keyUp('win')
        
    @staticmethod
    def win_q():
        """
        win + q : 呼叫windows快捷鍵，開啟系統搜尋功能
        :return:
        """
        keyDown('win')
        press('q')
        keyUp('win')

    @staticmethod
    def win_e():
        """
        win + e : 呼叫windows快捷鍵，開啟檔案總管
        :return:
        """
        keyDown('win')
        press('e')
        keyUp('win')

    @staticmethod
    def win_3():
        """
        win + 3 : 開啟指定應用程式
        :return:
        """
        keyDown('win')
        press('3')
        keyUp('win')

    @staticmethod
    def win_tab():
        """
        win + tab : 切換桌面
        :return:
        """
        keyDown('win')
        press('tab')
        keyUp('win')

    @staticmethod
    def ctrl_wave():
        """
        ctrl + ` : 自訂快捷鍵
        :return:
        """
        keyDown('ctrl')
        press('`')
        keyUp('ctrl')


if __name__ == "__main__":
    FuncKey.win_3()
