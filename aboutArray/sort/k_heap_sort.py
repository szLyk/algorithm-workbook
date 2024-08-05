#  已知一个几乎有序（几乎有序: 如果把数组排好顺序的话 每个元素移动的距离可以不超过k 并且K相对于数组来说比较小）的数组
# 请选择一个合适的排序方法进行排序
import heapq
import random


# 生成数组
def generate_almost_sorted_array(length, k):
    # 创建一个有序数组
    array = list(range(1, length + 1))

    # 对于每个元素，决定是否移动以及移动的距离
    for i in range(length):
        if random.random() < 0.5:  # 50%的概率移动
            direction = random.choice([-1, 1])  # 随机选择方向
            distance = random.randint(1, k)  # 移动的距离
            new_pos = i + direction * distance

            # 确保新位置在数组范围内
            if 0 <= new_pos < length:
                # 移动元素
                array.insert(new_pos, array.pop(i))

    return array


def sort_almost_sorted(arr, k):
    # 初始化一个小顶堆，包含数组的前 k+1 个元素
    heap = arr[:k + 1]
    heapq.heapify(heap)

    # 初始化已排序部分
    sorted_arr = []

    # 处理除了前 k+1 个元素外的所有元素
    for i in range(k + 1, len(arr)):
        # 弹出堆顶元素并添加到已排序数组
        sorted_arr.append(heapq.heappop(heap))
        # 将当前元素添加到堆中
        heapq.heappush(heap, arr[i])

    # 处理剩下的堆
    while heap:
        sorted_arr.append(heapq.heappop(heap))

    return sorted_arr


# 生成一个长度为 20 的几乎有序数组，其中 k=6
array_length = 20
k = 6
almost_sorted_array = generate_almost_sorted_array(array_length, k)
print(sort_almost_sorted(almost_sorted_array, k))
