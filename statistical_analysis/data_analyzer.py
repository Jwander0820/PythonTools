import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from statistics import mean, median, stdev, variance


class DataAnalyzer:
    def __init__(self, data, remove_zero=False):
        self.data = self._remove_zero(data) if remove_zero else data
        self.counter = Counter(self.data)

    def _remove_zero(self, data):
        """
        移除接近 0 之極小值(包含 0 )
        :param data:
        :return:
        """
        return [x for x in data if abs(x) > 1e-9]

    def general_statistics(self):
        common_mode, common_mode_count = self.counter.most_common(1)[0]
        general_mean = mean(self.data)
        general_median = median(self.data)
        general_stdev = stdev(self.data)
        general_variance = variance(self.data)
        min_value = min(self.data)
        max_value = max(self.data)
        sum_value = sum(self.data)
        count_value = len(self.data)

        return {
            "眾數": [common_mode, common_mode_count],
            "一般平均": round(general_mean, 5),
            "中位數": round(general_median, 5),
            "標準差": round(general_stdev, 5),
            "變異數": round(general_variance, 5),
            "最小值": round(min_value, 5),
            "最大值": round(max_value, 5),
            "總和": round(sum_value, 5),
            "數量": count_value
        }

    def special_statistics(self):
        """
        特殊規則下的平均值，篩選掉 0 值 與 絕對值大於 5 之值後計算平均
        :return:
        """
        special_mean_data = [x for x in self.data if abs(x) <= 5 and x != 0]
        special_mean = mean(special_mean_data) if special_mean_data else "Not applicable"

        return {
            "特殊平均": round(special_mean, 5)
        }

    def plot_distribution(self, mode='fixed', n_bins=None, bin_width=1):
        """
        繪製直方圖
        :param mode:模式選擇; fixed/dynamic; fixed為固定寬度、dynamic為動態寬度須設定區間總數
        :param n_bins: 設定動態模式下的區間總數，設定為10則代表最大值與最小值之間等分10個區間
        :param bin_width: 設定固定模式下的區間寬度，設定為1即間隔為1做一個區間
        :return:
        """
        min_val, max_val = min(self.data), max(self.data)

        if mode == 'fixed':
            bins = np.arange(min_val, max_val + bin_width, bin_width)
        elif mode == 'dynamic':
            bins = n_bins if n_bins else 10  # 可以設定其他預設的bin數量

        plt.hist(self.data, bins=bins, edgecolor='black')
        plt.xlabel('Angle')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()

        print(f"最小值: {min_val}, 最大值: {max_val}")
        if mode == 'fixed':
            print(f"區間大小: {bin_width}")
        else:
            print(f"區間數量: {bins}")

    def plot_line_graph(self, x_data=None, y_label='Value', x_label='Index', title='Line Graph'):
        """
        繪製折線圖
        :param x_data: x軸的數據，若為None則使用索引
        :param y_label: y軸的標籤
        :param x_label: x軸的標籤
        :param title: 圖的標題
        """
        if x_data is None:
            x_data = list(range(len(self.data)))

        plt.plot(x_data, self.data, marker='o', linestyle='-', linewidth=2, markersize=8)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.grid(True)
        plt.show()

if __name__ == '__main__':
    _data = [-3.89, -3.46, 0.54, 1.14, 5.11, 0]
    analyzer = DataAnalyzer(_data, remove_zero=True)

    general_stats = analyzer.general_statistics()
    print(f"一般統計: {general_stats}")

    special_stats = analyzer.special_statistics()
    print(f"特殊統計: {special_stats}")

    analyzer.plot_distribution(bin_width=1)

    analyzer.plot_line_graph()