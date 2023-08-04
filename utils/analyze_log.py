import re


class LogAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.threshold = None
        self.keyword = None

    def set_keyword(self, keyword):
        """
        設定關鍵字(可改進方向: 多關鍵字檢測、組合關鍵字條件檢測)
        :param keyword: 關鍵字
        :return:
        """
        self.keyword = keyword

    def keyword_filter(self, line):
        """
        檢測 log 內特定關鍵字
        :param line:文字段落
        :return:
        """
        return self.keyword in line if self.keyword else False

    def threshold_filter(self, line):
        """
        檢測 log 內清單值是否有大於閾值之值
        :param line:文字段落
        :return:
        """
        match = re.search(r'\[\s*([\d\.\-\,\s]+)\s*\]', line)
        if match:
            list_str = match.group(1)
            list_values = [float(x) for x in list_str.split(',')]
            return max(list_values) > self.threshold
        return False

    def log_level_filter(self, line):
        """
        檢測 log 內是否包含新的日誌級別關鍵字
        :param line:文字段落
        :return:
        """
        log_level_keywords = ['DEBUG', 'WARNING', 'INFO', 'ERROR']
        return any(keyword in line for keyword in log_level_keywords)

    def analyze_with_keyword(self):
        """
        檢測 log 內特定關鍵字，並收集該關鍵字後的所有行，直到遇到下一個關鍵字或檔案結束
        :return:
        """
        error_dict = {}
        collecting = False
        error_messages = []
        error_line = None

        with open(self.file_path, 'r', encoding="utf8") as f:
            for line_number, line in enumerate(f, start=1):
                if self.keyword_filter(line):
                    if collecting:  # 如果正在收集錯誤訊息，則先將已收集的錯誤訊息存儲起來
                        error_dict[error_line] = error_messages
                        error_messages = []
                    collecting = True
                    error_line = line_number
                    error_messages.append(line.strip())  # 將包含 'ERROR' 的當下那一行加入到錯誤訊息中
                elif self.log_level_filter(line):  # 如果遇到新的日誌級別關鍵字，則停止收集錯誤訊息
                    if collecting:
                        error_dict[error_line] = error_messages
                        error_messages = []
                        collecting = False
                elif collecting:  # 如果正在收集錯誤訊息，則將當前行添加到錯誤訊息列表中
                    error_messages.append(line.strip())

            if collecting:  # 如果檔案結束時正在收集錯誤訊息，則將已收集的錯誤訊息存儲起來
                error_dict[error_line] = error_messages

        for error_line, error_messages in error_dict.items():
            print(f"Line {error_line}:")
            for message in error_messages:
                print(message)
            print(f"\n-----------錯╰(*°▽°*)╯啦-----------\n")

        return error_dict

    def analyze_with_keyword_and_threshold(self, threshold=3):
        """
        檢測 log 內特定關鍵字(可選) + 清單值是否有大於閾值之值
        主要是用於檢測歪斜校正的清單中是否有大於閾值之值
        :param threshold:
        :return:
        """
        self.threshold = threshold
        with open(self.file_path, 'r', encoding="utf8") as f:
            for line_number, line in enumerate(f, start=1):
                if self.keyword:
                    if self.keyword_filter(line) and self.threshold_filter(line):
                        print(f"Line {line_number}: {line}")
                else:
                    if self.threshold_filter(line):
                        print(f"Line {line_number}: {line}")


if __name__ == '__main__':
    path = r"C:\Users\jasper chiu\Downloads\2023-08-04_太虛法師文鈔(世論)_內文_py.log"

    analyzer = LogAnalyzer(path)
    analyzer.set_keyword('ERROR')
    error_dict = analyzer.analyze_with_keyword()
