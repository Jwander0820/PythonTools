import time
import pyautogui
from func_key import FuncKey


class AutoControl:
    @staticmethod
    def auto_move_mail_to_other_desktop():
        img_folder = './click_img'
        FuncKey.win_tab()
        time.sleep(1)

        if pyautogui.locateCenterOnScreen(f'{img_folder}/chrome_logo_3.png'):  # 若有檢測到chrome logo的座標，點擊該座標
            pyautogui.click((pyautogui.locateCenterOnScreen(f'{img_folder}/chrome_logo_3.png')))

        time.sleep(1)
        if pyautogui.locateCenterOnScreen(f'{img_folder}/keep_logo_2.png'):  # 檢測圖標1，若沒有檢測到，則切換另一種檢測圖標
            pyautogui.click((pyautogui.locateCenterOnScreen(f'{img_folder}/keep_logo_2.png')))  # 在keep網頁
            pyautogui.dragRel(0, 200, 0.5)  # 0.5秒內向下移動200pixel
            pyautogui.moveRel(400, 0)  # 滑鼠向右相對位移400pixel
            pyautogui.dragRel(0, -400, 0.5)  # 0.5秒內向上移動400pixel
        else:
            pyautogui.click((pyautogui.locateCenterOnScreen(f'{img_folder}/keep_logo_3.png')))  # 不在keep網頁
            pyautogui.dragRel(0, 200, 0.5)
            pyautogui.moveRel(400, 0)
            pyautogui.dragRel(0, -400, 0.5)

        time.sleep(1)
        FuncKey.win_tab()

        time.sleep(1)
        pyautogui.moveTo((pyautogui.locateCenterOnScreen(f'{img_folder}/chrome_mail_logo.png')))  # 移動到郵件圖示的座標

        # 右鍵點擊指定網頁，將其移至另一桌面
        time.sleep(0.5)
        point = pyautogui.locateCenterOnScreen(f'{img_folder}/chrome_mail_logo.png')  # 取得郵件圖示的座標
        if point:
            pyautogui.click(point, button="right")  # 在指定座標點擊右鍵
            time.sleep(0.5)
            pyautogui.moveRel((50, 150))  # 移動滑鼠座標到"移至"的功能鍵上
            time.sleep(0.5)
            pyautogui.click()  # 點擊"移至"
            time.sleep(1)
            pyautogui.moveRel((420, 0))  # 滑鼠向右相對位移420pixel
            time.sleep(0.5)
            pyautogui.click(clicks=2)  # 點擊移至指定的桌面，一定秒數緩衝時間
            time.sleep(2)
        FuncKey.win_tab()  # 完成所有動作後 win+tab 回復原始狀態

    @staticmethod
    def auto_move_app_to_other_desktop():
        img_folder = './click_img'
        FuncKey.win_tab()
        time.sleep(1.5)

        # 右鍵點擊指定網頁，將其移至另一桌面
        point = pyautogui.locateCenterOnScreen(f'{img_folder}/donotsleep_logo.png')  # 取得APP圖示的座標
        if point:
            x, y = point  # 取得圖示座標後，向右下移動(150, 150)，因為圖標無法使用右鍵功能，所以需要移動到視窗位置執行功能
            x = x + 150
            y = y + 150
            time.sleep(0.5)
            pyautogui.click((x, y), button="right")  # 在指定座標點擊右鍵
            time.sleep(0.5)
            pyautogui.moveRel((50, 150))  # 移動滑鼠座標到"移至"的功能鍵上
            time.sleep(0.5)
            pyautogui.click()  # 點擊"移至"
            time.sleep(1)
            pyautogui.moveRel((420, 50))  # 滑鼠向右相對位移420pixel，向下移動50pixel，移動到第三桌面
            time.sleep(0.5)
            pyautogui.click(clicks=2)  # 點擊移至指定的桌面
            time.sleep(2)
        FuncKey.win_tab()  # 完成所有動作後 win+tab 回復原始狀態


if __name__ == "__main__":
    # AutoControl.auto_move_mail_to_other_desktop()
    AutoControl.auto_move_app_to_other_desktop()
