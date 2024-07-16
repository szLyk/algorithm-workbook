# 插入排序：将数组分为已排序和未排序两部分，从未排序部分取出元素插入到已排序部分的正确位置
one_array = [5, 1, 6, 8, 4, 2, 3, 9, 1]

for i in range(1, len(one_array)):
    key = one_array[i]
    j = i - 1
    while j >= 0 and one_array[j] > key:
        one_array[j + 1] = one_array[j]
        j -= 1
    one_array[j + 1] = key

print(one_array)
