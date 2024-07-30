# 快排 同样是分治策略，通过选择一个“基准”元素将数组分为两部分，左边小于基准，右边大于基准，然后递归排序两边

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


# 测试
one_array = [5, 1, 4, 6, 4, 2, 3, 9, 1]
sorted_array = quick_sort(one_array)
print(sorted_array)  # 输出 [1, 1, 2, 3, 4, 4, 5, 6, 9]
