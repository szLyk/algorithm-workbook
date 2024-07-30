#  小和问题: 在数组中 每一个数比左边当前数小的树累加起来，叫做这个数组的小和
#  正向思维：起始位置 往左遍历 对小于该数的数求总和 最后累加
#  反向思维：起始位置x 遍历往右看 有多少数比该数大 则x * n 最后求总和 => 用分治的思维来做

def small_sum(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_sum = small_sum(arr[:mid])
    right, right_sum = small_sum(arr[mid:])

    merged, merge_sum = merge_and_count(left, right)
    return merged, left_sum + right_sum + merge_sum


def merge_and_count(left, right):
    i = j = 0
    merged = []
    sum_value = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            sum_value += left[i] * (len(right) - j)
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged, sum_value


# 测试
one_array = [5, 1, 4, 6, 4, 2, 3, 9, 1]
sorted_array, total_sum = small_sum(one_array)
print(sorted_array)  # 输出排序后的数组
print(total_sum)  # 输出小和
