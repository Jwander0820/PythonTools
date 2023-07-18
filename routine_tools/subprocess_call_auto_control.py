from time import sleep
from subprocess import run


def call_auto_control():
    """
    使用subprocess呼叫並執行指定py檔案
    """
    # 在cmd_input前添加指向該環境python.exe的路徑即可開啟對應的虛擬環境(main那邊就不需要#!指向環境了(可有可無))
    cwd = r"C:\JasperWork\Tools\PythonTools\routine_tools"  # 設定工作目錄(會影響import的路徑，因此設在與main.py同一層)
    env = r"C:\JasperWork\venv\PythonTools\Scripts\python.exe"  # 指向venv_tensorflow虛擬環境
    call = rf"{cwd}\routine_boot_work.py"
    # 輸入參數 # cmd第一行沒有加python的話，預設是會當前的環境變數
    cmd_input = [env, call]
    # 執行
    run(cmd_input, shell=True, cwd=cwd)


if __name__ == '__main__':
    call_auto_control()
    # 將subprocess壓成exe去呼叫指定程式，之後修改指定程式時不用重新壓exe
    # pyinstaller -F .\routine_tools\subprocess_call_auto_control.py
