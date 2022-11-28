import time
from func_key import FuncKey
from auto_mouse_control import auto_move_mail_to_other_desktop


def main():
    time.sleep(60)
    auto_move_mail_to_other_desktop()
    time.sleep(5)
    FuncKey.win_3()


if __name__ == "__main__":
    main()
