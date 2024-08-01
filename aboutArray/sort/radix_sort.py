# 一种非比较型整数排序算法，它通过将整数按位数切割成不同的数字，然后按每个位数进行排序来实现整个排序过程。基数排序适用于非负整数，且在处理大数据集时非常高效，尤其是在位数较少的情况下.
import math

# 测试
one_array = [51, 100, 4, 16, 47, 22, 43, 119, 9]


# 获取最大位数
def get_max_digits(some_array):
    max_digits = -1
    for i in range(len(some_array) - 1):
        num = some_array[i]
        digits = math.floor(math.log10(num)) + 1
        if digits > max_digits:
            max_digits = digits
    return max_digits


def count_num_frequency(some_array):
    new_array = [10]


print(get_max_digits(one_array))
