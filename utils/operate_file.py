import os
import shutil

import pandas as pd


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

    @staticmethod
    def copy_file(src_path: str, dst_path: str):
        """
        從來源路徑複製檔案或目錄到目標路徑。
        :param src_path: 來源路徑，可以是檔案或目錄
        :param dst_path: 目標路徑
        :return: 無
        """
        if os.path.isfile(src_path):
            # 如果來源路徑是檔案，則複製檔案
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            shutil.copy2(src_path, dst_path)  # copy2 會保留原文件的 metadata
        elif os.path.isdir(src_path):
            # 如果來源路徑是目錄，則複製整個目錄
            shutil.copytree(src_path, dst_path)

    @staticmethod
    def move_file(src_path: str, dst_path: str):
        """
        從來源路徑移動檔案或目錄到目標路徑。
        :param src_path: 來源路徑，可以是檔案或目錄
        :param dst_path: 目標路徑
        :return: 無
        """
        shutil.move(src_path, dst_path)

    @staticmethod
    def list_files_in_folder(folder_path: str) -> list[str]:
        """
        掃描指定資料夾內的檔案名稱
        :param folder_path: 要掃描的資料夾路徑
        :return: 檔案名稱的列表
        """
        try:
            file_names = os.listdir(folder_path)
            return file_names
        except FileNotFoundError:
            print(f"錯誤：找不到指定的資料夾 {folder_path}")
            return []
        except PermissionError:
            print(f"錯誤：無權訪問指定的資料夾 {folder_path}")
            return []

    @staticmethod
    def check_key_in_file_list(key: str, file_list: list[str]) -> bool:
        """
        檢查指定的 key 是否在檔案清單中
        :param key: 要搜尋的關鍵字
        :param file_list: 檔案名稱的列表
        :return: 如果關鍵字在檔案清單中，則返回 True，否則返回 False
        """
        for file_name in file_list:
            if key in file_name:
                return True
        return False

    @staticmethod
    def write_data_to_excel(data, file_name: str = "output.xlsx") -> None:
        """
        將資料（清單或字典）寫入到Excel文件中。

        :param data: 需要寫入Excel的資料，可以是清單或字典。
        :param file_name: Excel文件的名稱，包括副檔名（例如：output.xlsx）。
        """
        if isinstance(data, list):
            df = pd.DataFrame(data, columns=['Data'])
        elif isinstance(data, dict):
            df = pd.DataFrame(list(data.items()), columns=['Key', 'Data'])
        else:
            raise ValueError("Unsupported data type. Please provide a list or dictionary.")

        # 將DataFrame寫入Excel文件
        df.to_excel(file_name, index=False)

    @staticmethod
    def list_files_and_folders(directory):
        """
        遍歷並列印指定資料夾下所有檔案和資料夾

        這個方法將會遍歷指定的資料夾，並遞迴地訪問所有子資料夾和檔案
        對於每個訪問的資料夾，它會列出資料夾的路徑，然後分別列出其下所有子資料夾和檔案的路徑

        :param directory:要遍歷的資料夾的路徑
        :return:
        """
        # 遍歷指定資料夾
        for root, dirs, files in os.walk(directory):
            # 顯示目前資料夾的路徑
            print(f"當前資料夾: {root}")
            # 顯示子資料夾
            for dir in dirs:
                print(f"子資料夾: {os.path.join(root, dir)}")
            # 顯示檔案
            for file in files:
                print(f"檔案: {os.path.join(root, file)}")

    @staticmethod
    def remove_ipynb_checkpoints(directory):
        """
        遍歷指定資料夾及其所有子資料夾，並刪除找到的任何 `.ipynb_checkpoints` 資料夾

        `.ipynb_checkpoints` 資料夾通常由Jupyter Notebook自動創建，用於保存未提交的更改。
        這些資料夾有時可能會導致版本控制或模型訓練時的問題，特別是在進行路徑導入和文件處理時。
        這個方法可以幫助維護乾淨的工作目錄，避免這些問題。

        :param directory:要清理的資料夾的路徑
        :return:
        """
        # 清除資料夾下的 .ipynb_checkpoints 避免模型訓練時匯入導致錯誤
        for root, dirs, files in os.walk(directory, topdown=False):
            # 檢查是否有 .ipynb_checkpoints 資料夾
            if '.ipynb_checkpoints' in dirs:
                checkpoint_path = os.path.join(root, '.ipynb_checkpoints')
                # 刪除 .ipynb_checkpoints 資料夾
                shutil.rmtree(checkpoint_path)
                print(f"已刪除: {checkpoint_path}")


if __name__ == '__main__':
    _create_folder = "./upper_folder/test_folder"
    OperateFile.create_folder(_create_folder)  # 建立資料夾
    _clear_folder = "./upper_folder"
    OperateFile.clear_folder(_clear_folder)  # 清空資料夾

    # 列出當前資料夾下所有檔案，並寫入xlsx檔案
    _folder_path = "./"
    _file_list = OperateFile.list_files_in_folder(_folder_path)
    OperateFile.write_data_to_excel(_file_list, "output.xlsx")
