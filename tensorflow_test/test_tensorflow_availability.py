import tensorflow as tf

# 列出可用的 GPU 裝置
print("Available GPUs:", tf.config.list_physical_devices('GPU'))

# 檢查 TensorFlow 是否使用 GPU 計算
print("TensorFlow uses GPU:", tf.test.is_gpu_available())

# 計算測試
# 定義常量
a = tf.constant(2)
b = tf.constant(3)

# 定義運算
@tf.function
def add_op(x, y):
    return x + y

# 執行運算
result = add_op(a, b)

print(result)
