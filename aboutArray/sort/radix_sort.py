# 一种非比较型整数排序算法，它通过将整数按位数切割成不同的数字，然后按每个位数进行排序来实现整个排序过程。基数排序适用于非负整数，且在处理大数据集时非常高效，尤其是在位数较少的情况下.
import math
import sys

# 测试
one_array = [51, 100, 4, 16, 47, 22, 43, 119, 9, -10]
max_length = 10001
base = 10


# 获取最大位数
def get_max_digits(some_array):
    max_value = -sys.maxsize - 1
    min_value = sys.maxsize
    for i in range(len(some_array)):
        if some_array[i] > max_value:
            max_value = some_array[i]
        if some_array[i] < min_value:
            min_value = some_array[i]
    if min_value < 0:
        for i in range(len(some_array)):
            some_array[i] -= min_value
        max_value -= min_value
    max_digits = math.floor(math.log10(max_value)) + 1

    return max_digits, min_value, some_array


def radix_sort(some_array):
    # 如果数组为空或只有一个元素，直接返回
    if len(some_array) <= 1:
        return some_array

    digits_and_min_and_array = get_max_digits(some_array)
    some_array = digits_and_min_and_array[2]
    digits = digits_and_min_and_array[0]
    min_value = digits_and_min_and_array[1]
    length = len(some_array)
    help_array = [0] * length
    for digit in range(digits):
        count_array = [0] * 10
        for index in range(len(some_array)):
            #  获取不同位数上的数字
            value = int(some_array[index] / int(base ** digit)) % base
            count_array[value] += 1
        # 统计大于等于当前位置的数有多少个
        for i in range(1, len(count_array)):
            count_array[i] += count_array[i - 1]

        for j in range(length - 1, -1, -1):
            value = int(some_array[j] / int(base ** digit)) % base
            idx = count_array[value] - 1
            help_array[idx] = some_array[j]
            count_array[value] -= 1
        some_array = help_array[:]

    if min_value < 0:
        for i in range(len(some_array) - 1):
            some_array[i] += min_value
    return some_array


print(radix_sort(one_array))
