from time import sleep
import subprocess


def call_auto_control():
    """
    使用subprocess，模擬cmd輸入參數調用Revital(測試版本)
    """
    # 在cmd_input前添加指向該環境python.exe的路徑即可開啟對應的虛擬環境(main那邊就不需要#!指向環境了(可有可無))
    cwd = r"E:\JasperWork\Github\PythonTools\routine_tools"  # 設定工作目錄(會影響import的路徑，因此設在與main.py同一層)
    env = r"E:\JasperWork\project\GestureRecognitionControl\Scripts\python.exe"  # 指向venv_tensorflow虛擬環境
    call1 = rf"{cwd}\auto_mouse_control.py"
    call2 = rf"{cwd}\auto_open_app.py"
    # 輸入參數 # cmd第一行沒有加python的話，預設是會當前的環境變數
    cmd_input_1 = [env, call1]
    cmd_input_2 = [env, call2]
    # 執行
    sleep(60)
    subprocess.run(cmd_input_1, shell=True, cwd=cwd, stdout=subprocess.PIPE)
    sleep(5)
    subprocess.run(cmd_input_2, shell=True, cwd=cwd, stdout=subprocess.PIPE)


if __name__ == '__main__':
    call_auto_control()
