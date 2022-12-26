import time
import pyautogui
from func_key import FuncKey


class AutoControl:
    @staticmethod
    def auto_move_mail_to_other_desktop():
        img_folder = './click_img'
        FuncKey.win_tab()
        time.sleep(1)

        if pyautogui.locateCenterOnScreen(f'{img_folder}/chrome_logo_5.png'):  # 若有檢測到chrome logo的座標，點擊該座標
            pyautogui.click((pyautogui.locateCenterOnScreen(f'{img_folder}/chrome_logo_5.png')))
        elif pyautogui.locateCenterOnScreen(f'{img_folder}/chrome_logo_4.png'):
            pyautogui.click((pyautogui.locateCenterOnScreen(f'{img_folder}/chrome_logo_4.png')))
        else:
            FuncKey.enter()  # 若都無檢測到chrome，按下enter中止win+tab的狀態
        time.sleep(1)

        pyautogui.moveTo(60, 30)
        pyautogui.click((60, 30), button="right")  # 在指定座標點擊右鍵(左上角網頁)
        time.sleep(1)

        keyboard_list = ["down", "down", "down", "down", "enter", "enter"]  # 點擊右鍵後透過鍵盤方向鍵操作移動視窗
        AutoControl.continuous_keyboard_control(*keyboard_list)  # 將分頁移動到其他視窗
        time.sleep(1)

        FuncKey.win_tab()
        time.sleep(0.5)

        keyboard_list = ["right", "right_click", "down", "down", "right", "enter"]  # 將視窗移動到另一桌面
        AutoControl.continuous_keyboard_control(*keyboard_list)
        time.sleep(1)

        FuncKey.win_tab()  # 完成所有動作後 win+tab 回復原始狀態

    @staticmethod
    def auto_move_app_to_other_desktop():
        img_folder = './click_img'
        FuncKey.win_tab()
        time.sleep(1.5)

        # 右鍵點擊指定網頁，將其移至另一桌面
        point = pyautogui.locateCenterOnScreen(f'{img_folder}/donotsleep_logo2.png')  # 取得APP圖示的座標
        if point:
            x, y = point  # 取得圖示座標後，向右下移動(150, 150)，因為圖標無法使用右鍵功能，所以需要移動到視窗位置執行功能
            x = x + 750  # win 11 可以透過圖標觸發右鍵功能，但此處仍做保留
            y = y + 150
            time.sleep(0.5)
            pyautogui.click((x, y), button="right")  # 在指定座標點擊右鍵
            time.sleep(1)  # 點擊右鍵後透過鍵盤方向鍵操作移動視窗

            keyboard_list = ["down", "down", "right", "down", "enter"]
            AutoControl.continuous_keyboard_control(*keyboard_list)
            time.sleep(1)
        FuncKey.win_tab()  # 完成所有動作後 win+tab 回復原始狀態

    @staticmethod
    def continuous_keyboard_control(*args, interval=0.2):
        """
        自動連續輸入方向鍵或Enter的指令
        :param args:複數的操作指令(只包含方向鍵與Enter)，會依序執行移動操作
        :param interval:操作的間隔時間，預設為0.2秒
        :return:
        """
        for key in args:
            if key == "up":
                FuncKey.up()
            elif key == "down":
                FuncKey.down()
            elif key == "left":
                FuncKey.left()
            elif key == "right":
                FuncKey.right()
            elif key == "enter":
                FuncKey.enter()
            elif key == "right_click":
                FuncKey.right_click()
            time.sleep(interval)


if __name__ == "__main__":
    # AutoControl.auto_move_mail_to_other_desktop()
    AutoControl.auto_move_app_to_other_desktop()
