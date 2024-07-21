#  荷兰国旗问题
#  给定一个数组和一个数 要求用O(N)的时间复杂度 和 O(1)的额外时间复杂度 将大于该数的放到数组的右边 小于该数的放到数组的左边

def partition_array(arr, num):
    left = 0
    right = len(arr) - 1

    while left <= right:
        while left <= right and arr[left] < num:
            left += 1
        while left <= right and arr[right] >= num:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr


# 测试
one_array = [5, 1, 4, 6, 4, 2, 3, 9, 1]
num = 4
result = partition_array(one_array, num)
print(result)  # 输出 [1, 1, 3, 2, 4, 6, 4, 9, 5] （大于4的在右边，小于4的在左边）
