# 一种非比较型整数排序算法，它通过将整数按位数切割成不同的数字，然后按每个位数进行排序来实现整个排序过程。基数排序适用于非负整数，且在处理大数据集时非常高效，尤其是在位数较少的情况下.

# 测试
one_array = [5, 1, 4, 6, 4, 2, 3, 9, 1]


def merge_sort(some_array):
    length = len(some_array)
