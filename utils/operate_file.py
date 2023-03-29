import os
import shutil


class OperateFile:
    @staticmethod
    def clear_folder(folder_path):
        """
        清空指定資料夾下的所有資料。如果資料夾存在，則刪除資料夾中的所有檔案和子資料夾。
        :param folder_path: 要清空的資料夾路徑。
        """
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
        else:
            print(f"資料夾 {folder_path} 不存在或不是一個有效的資料夾。")

    @staticmethod
    def create_folder(*args):
        """
        批量建立資料夾
        :param args: 建立資料夾的路徑
        :return:
        """
        try:
            for folder in args:
                # 若資料夾不存在則建立資料夾
                if not os.path.exists(folder):
                    os.makedirs(folder)
            return True
        except Exception as e:
            print(f"ERROR: {e}")
            return False


if __name__ == '__main__':
    _create_folder = "./upper_folder/test_folder"
    OperateFile.create_folder(_create_folder)  # 建立資料夾
    _clear_folder = "./upper_folder"
    OperateFile.clear_folder(_clear_folder)  # 清空資料夾
