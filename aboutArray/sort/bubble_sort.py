# 冒泡排序 通过重复遍历要排序的列表，比较相邻元素并交换位置
one_array = [1, 5, 6, 8, 4, 2, 3, 9, 1]
for j in range(len(one_array) - 1):
    for i in range(len(one_array) - 1 - j):
        a = one_array[i]
        b = one_array[i + 1]
        if a > b:
            a ^= b
            b ^= a
            a ^= b
        one_array[i] = a
        one_array[i + 1] = b
print(one_array)
