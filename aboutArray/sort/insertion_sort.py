# 插入排序：将数组分为已排序和未排序两部分，从未排序部分取出元素插入到已排序部分的正确位置
one_array = [5, 1, 4, 6, 4, 2, 3, 9, 1]

for i in range(len(one_array)):
    key = one_array[i]
    j = i - 1
    while j >= 0 and key <= one_array[j]:
        one_array[j + 1] = one_array[j]  # 当前数后移
        j -= 1  # 往前一个数和现在的数进行比较
    one_array[j+1] = key

print(one_array)
