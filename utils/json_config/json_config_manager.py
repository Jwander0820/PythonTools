import json


class JsonConfigReader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.config_data = self.load_config(file_path)

    def load_config(self, file_path: str) -> dict:
        """
        讀取指定的 JSON 檔案並將其內容轉換為字典
        :param file_path: 要讀取的 JSON 檔案路徑
        :return: JSON 檔案內容對應的字典
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data

    def get_env_config(self) -> dict:
        """
        根據 ENV 屬性值獲取當前環境的設定。
        """
        env = self.config_data["ENV"]
        env_config = self.config_data[env]
        return env_config

    def get_value(self, key: str) -> str:
        """
        根據鍵值獲取當前環境設定中的特定值。
        """
        env_config = self.get_env_config()
        return env_config.get(key, "")

    def get_all_configs(self) -> dict:
        """
        獲取 JSON 設定檔中的所有設定。
        """
        return self.config_data


if __name__ == "__main__":
    json_config_reader = JsonConfigReader("json_config.json")
    print("Current environment config:", json_config_reader.get_env_config())
    print("ApiUrl value in current environment config:", json_config_reader.get_value("ApiUrl"))
    print("All configs:", json_config_reader.get_all_configs())
