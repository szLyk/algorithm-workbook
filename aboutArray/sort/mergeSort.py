#  归并排序 使用分治策略，将数组分为两半，递归地排序两边，然后合并

def merge_sort(arr):
    # 如果数组长度小于等于1，直接返回
    if len(arr) <= 1:
        return arr

    # 找到数组的中间位置
    mid = len(arr) // 2

    # 递归地排序左半部分和右半部分
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # 合并两个有序的子数组
    return merge(left_half, right_half)


def merge(left, right):
    sorted_arr = []
    i = j = 0

    # 合并两个有序数组
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # 如果左半部分还有剩余，添加到结果中
    while i < len(left):
        sorted_arr.append(left[i])
        i += 1

    # 如果右半部分还有剩余，添加到结果中
    while j < len(right):
        sorted_arr.append(right[j])
        j += 1

    return sorted_arr


# 测试
one_array = [5, 1, 4, 6, 4, 2, 3, 9, 1]
sorted_array = merge_sort(one_array)
print(sorted_array)  # 输出 [1, 1, 2, 3, 4, 4, 5, 6, 9]
