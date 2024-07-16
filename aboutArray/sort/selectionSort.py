# 选择排序：每次从未排序的部分选出最小（或最大）的元素放到已排序序列的末尾
one_array = [1, 5, 6, 8, 4, 2, 3, 9, 1]
for i in range(len(one_array)):
    a = one_array[i]
    for j in range(i + 1, len(one_array)):
        b = one_array[j]
        if a > b:
            a ^= b
            b ^= a
            a ^= b
            one_array[i] = a
            one_array[j] = b
print(one_array)
