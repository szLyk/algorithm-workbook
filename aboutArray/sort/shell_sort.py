#  希尔排序：插入排序的一种扩展，通过间隔跳跃式的比较和交换来加速排序过程

one_array = [5, 1, 4, 6, 4, 2, 3, 9, 1]

length = len(one_array)
gap = length >> 1

while gap > 0:

    for i in range(gap, length):
        tmp = one_array[i]
        j = i
        while j >= gap and one_array[j - gap] > tmp:
            one_array[j] = one_array[j - gap]
            j -= gap
        one_array[j] = tmp
    gap >>= 1

print(one_array)