import webbrowser
import time
import subprocess


def open_start_browser():
    """
    自動開啟起始瀏覽器頁面
    :return:
    """
    # 指定你的chrome路徑
    chromePath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

    # 註冊Chrome
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))

    # 指定Chrome開啟網頁
    # 開啟keep
    webbrowser.get('chrome').open('https://keep.google.com/#home', new=1)
    time.sleep(1)
    # 開啟outlook
    webbrowser.get('chrome').open('https://outlook.office.com/mail/', new=1)
    time.sleep(1)
    # 開啟onedrive
    webbrowser.get('chrome').open('https://beltom-my.sharepoint.com/personal/jasper_chiu_beltom_com_tw/_layouts/15/onedrive.aspx?login_hint=Jasper%2EChiu%40beltom%2Ecom%2Etw', new=1)


def open_start_explorer():
    """
    自動開啟起始檔案總管與應用程式
    :return:
    """
    # 開啟檔案總管 - 下載
    subprocess.Popen(r'explorer "C:\Users\jasper chiu\Downloads"')
    time.sleep(1)
    # 開啟檔案總管 - Revital
    subprocess.Popen(r'explorer "E:\JasperWork\Revital"')
    time.sleep(1)
    # 開啟應用程式 - PyCharm
    subprocess.Popen(r'explorer "E:\JasperWork\PyCharm\PyCharm Community Edition 2022.2.2\bin\pycharm64.exe"')
    time.sleep(1)
    # 開啟應用程式 - DoNotSleep
    subprocess.Popen(r'explorer "E:\JasperWork\Github\PythonTools\dist\AutoShakeMouse.exe"')


if __name__ == "__main__":
    open_start_browser()
    open_start_explorer()
