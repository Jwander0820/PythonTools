import webbrowser
import time
import subprocess


class AutoOpen:
    @staticmethod
    def start_browser():
        """
        自動開啟起始瀏覽器頁面
        :return:
        """
        # 指定你的chrome路徑
        chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

        # 註冊Chrome
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

        # 指定Chrome開啟網頁
        # 開啟keep
        webbrowser.get('chrome').open('https://keep.google.com/#home', new=1)
        time.sleep(1)
        # 開啟outlook
        webbrowser.get('chrome').open('https://outlook.office.com/mail/', new=1)
        time.sleep(1)
        # 開啟onedrive
        webbrowser.get('chrome').open('https://beltom-my.sharepoint.com/', new=1)

    @staticmethod
    def start_explorer():
        """
        自動開啟起始檔案總管與應用程式
        :return:
        """
        # 開啟檔案總管 - 下載
        subprocess.Popen(r'explorer "C:\Users\jasper chiu\Downloads"')
        time.sleep(1)
        # 開啟檔案總管 - Revital
        subprocess.Popen(r'explorer "C:\JasperWork\MainProject"')
        time.sleep(1)
        # 開啟應用程式 - PyCharm
        subprocess.Popen(r'explorer "C:\Software\PyCharm Community Edition 2022.3\bin\pycharm64.exe"')
        time.sleep(1)

    @staticmethod
    def start_app():
        """
        自動開啟起始應用程式(獨立)
        """
        # 開啟應用程式 - DoNotSleep
        cwd = r"C:\JasperWork\Tools\PythonTools\dist"
        subprocess.Popen(r'C:\JasperWork\Tools\PythonTools\dist\AutoShakeMouse.exe', cwd=cwd,
                         creationflags=subprocess.CREATE_NEW_CONSOLE)

    @staticmethod
    def auto_open_browser(*args):
        """
        以args的形式撰寫，可以輸入多個url，並開啟指定網站
        """
        # 指定你的chrome路徑
        chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        # 註冊Chrome
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        # 指定Chrome開啟網頁
        for url in args:
            print(url)
            webbrowser.get('chrome').open(f'{url}', new=1)
            time.sleep(1)


if __name__ == "__main__":
    # open_start_browser()
    # open_start_explorer()

    url1 = "https://keep.google.com/#home"
    url2 = "https://drive.google.com/drive/my-drive"
    AutoOpen.auto_open_browser(url1, url2)
