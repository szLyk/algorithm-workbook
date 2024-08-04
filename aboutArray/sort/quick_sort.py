# 快排 同样是分治策略，通过选择一个“基准”元素将数组分为两部分，左边小于基准，右边大于基准，然后递归排序两边
import random


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # 选择一个基准点（pivot）
    pivot = arr[len(arr) // 2]

    # 分割数组成三个部分：小于pivot的部分，等于pivot的部分，大于pivot的部分
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # 递归地对左右两部分进行快速排序，并将结果合并
    return quick_sort(left) + middle + quick_sort(right)


#  优解
def partition(arr, low, high):
    # 随机选择一个元素作为基准
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # 将基准元素移动到数组末尾

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pi = partition(arr, low, high)

        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)


# 测试
one_array = [5, 1, 4, 6, 4, 2, 3, 9, 1]
sorted_array = quick_sort(one_array)
print(sorted_array)  # 输出 [1, 1, 2, 3, 4, 4, 5, 6, 9]
# quick_sort2(one_array, 0, len(one_array) - 1)
print(quick_sort_inplace(one_array))
