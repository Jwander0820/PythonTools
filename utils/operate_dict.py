import json


class OperateDict:
    @staticmethod
    def open_json(data):
        """
        判斷傳入的是字典還是路徑（字符串）。若為路徑，則開啟JSON文件並回傳；已經為字典形式則直接回傳。

        :param data: 輸入的JSON文件路徑或字典
        :return: JSON DATA
        """
        # 如果輸入的是字符串，將其視為文件路徑並讀取文件
        if isinstance(data, str):
            try:
                with open(data, 'r', encoding='utf-8') as f:
                    json_data = json.load(f)
                return json_data
            except FileNotFoundError:
                print(f"File {data} not found")
            except json.JSONDecodeError:
                print(f"Invalid JSON file: {data}")
        # 如果輸入的是字典，直接返回
        elif isinstance(data, dict):
            return data
        else:
            print("Invalid input. Please provide a file path or a dictionary.")
            return None

    @staticmethod
    def save_json(data, file_name='test.json'):
        """
        將JSON格式的字符串或字典保存為.json文件。如果未指定文件名，則默認為test.json。

        :param data: 要保存的JSON格式字符串或字典
        :param file_name: 要保存的文件名（可選），默認為 'test.json'
        :return: None
        """
        # 如果輸入的是字符串，將其轉換為字典
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                print("Invalid JSON string")
                return
        # 將字典寫入文件
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def extract_keys_from_dict(original_dict: dict, *keys_to_extract: str) -> dict:
        """
        從原始字典中提取指定的鍵值對，並創建一個新字典。

        :param original_dict: 原始字典
        :param keys_to_extract: 要提取的鍵列表
        :return: 包含提取的鍵值對的新字典
        """
        new_dict = {key: original_dict[key] for key in keys_to_extract if key in original_dict}

        return new_dict

    @staticmethod
    def extract_keys_from_dict_split(original_dict: dict, *keys_to_extract: str) -> dict:
        """
        從原始字典中提取指定的鍵值對，並創建一個新字典。(拆分動作)

        :param original_dict: 原始字典
        :param keys_to_extract: 要提取的鍵列表
        :return: 包含提取的鍵值對的新字典
        """
        new_dict = {}

        for key in keys_to_extract:
            if key in original_dict:
                new_dict[key] = original_dict[key]

        return new_dict


if __name__ == '__main__':
    # 字典中提取特定鍵值資料組成新字典
    json_dict = {"name": "Jasper", "age": 25, "city": "Moon"}
    _new_dict = OperateDict.extract_keys_from_dict(json_dict, "name", "age")
    print(_new_dict)  # 輸出：{"name": "Jasper", "age": 25}

    # 儲存成json
    OperateDict.save_json(json_dict)  # 預設文件名為test.json

    # 開啟json檔案
    json_data = OperateDict.open_json("./test.json")
    print(json_data)
