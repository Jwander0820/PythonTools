import json
from collections import defaultdict, Counter


class JsonAnalyzer:
    def extract_nested_elements(self, data, key_to_extract):
        """
        從json資料中根據關鍵字，提取出指定的資料並組合成列表
        :param data: 原始資料
        :param key_to_extract:搜尋的關鍵字
        :return:
        """
        filter_data = defaultdict(list)
        self._recursive_extract(data, key_to_extract, filter_data)
        return filter_data

    def _recursive_extract(self, data, key_to_extract, filter_data):
        """
        這是一個遞迴函數，用於迴圈讀取JSON的字典和列表結構。
        如果遇到一個字典，它會查看每個鍵(key)是否與要提取的鍵(key_to_extract)相匹配。
        如果相匹配，就將該鍵的值添加到filter_data字典中。
        如果遇到一個列表，它會遍歷每個元素並對其運行相同的遞迴函數。
        這種方法的好處是您不需要知道元素的確切位置，函數會自動找到它們。
        :param data:原始資料
        :param key_to_extract:搜尋的關鍵字
        :param filter_data:儲存資料的字典
        :return:
        """
        if isinstance(data, dict):
            for key, value in data.items():
                if key == key_to_extract:
                    filter_data[key_to_extract].append(value)
                else:
                    self._recursive_extract(value, key_to_extract, filter_data)
        elif isinstance(data, list):
            for item in data:
                self._recursive_extract(item, key_to_extract, filter_data)


if __name__ == '__main__':
    # 從檔案載入 JSON 數據
    _data = {"level1": {"level2": {"key1": "value1", "key2": "value2",
                                   "level3": {"key1": "value3", "key3": "value4"}},
                        "level2_alt": {"key1": "value1", "key4": "value5"}}}

    analyzer = JsonAnalyzer()
    # 提取指定鍵值
    _filter_data = analyzer.extract_nested_elements(_data, "key1")

    print(_filter_data)
    # 計算指定鍵其值的頻率
    status_counter = Counter(_filter_data['key1'])
    print(status_counter)
