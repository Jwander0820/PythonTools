import time
from func_key import FuncKey
from auto_control_mouse import AutoControl
from auto_open_something import open_start_browser, open_start_explorer
from auto_create_work_log import create_work_log


def main():
    time.sleep(5)
    create_work_log()
    print("自動建立工作日誌")
    print("-------------_(´ཀ`」 ∠)-------------")

    time.sleep(5)
    open_start_browser()
    print("開啟起始瀏覽器與指定頁面")
    print("-------------Σ(っ °Д °;)っ-------------")

    time.sleep(60)
    AutoControl.auto_move_mail_to_other_desktop()
    print("自動執行移動分頁與將指定頁面移動至另一桌面的操作")
    print("-------------ψ(｀∇´)ψ-------------")

    time.sleep(5)
    open_start_explorer()
    print("開啟指定檔案總管與指定應用程式")
    print("-------------┌( ಠ_ಠ)┘-------------")

    time.sleep(5)
    AutoControl.auto_move_app_to_other_desktop()
    print("自動執行將指定APP移動至另一桌面的操作")
    print("-------------┌( ಠ_ಠ)┘-------------")

    time.sleep(10)
    FuncKey.win_3()
    print("快捷鍵開啟LINE")
    print("-------------(｡･∀･)ﾉﾞ-------------")

    time.sleep(1)
    print("\n\n\n          開機例行處理已完成")
    print("-------------╰(*°▽°*)╯-------------")
    time.sleep(5)


if __name__ == "__main__":
    main()
    