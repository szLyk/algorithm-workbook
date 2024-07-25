#  大根堆（也称为最大堆）是一种特殊的二叉树数据结构，其中每个节点的值都不小于其子节点的值。大根堆通常用于实现优先队列，并且在堆排序算法中扮演重要角色。
import math

# 大根堆的性质：
# 形状属性：大根堆是一棵完全二叉树，也就是说除了最后一层之外，每一层都是满的，并且最后一层的节点都尽可能地靠左。
# 堆序属性：对于任意节点i（除了叶子节点），都有heap[i] ≥ heap[2*i+1] 和 heap[i] ≥ heap[2*i+2]，其中2*i+1和2*i+2分别是i的左孩子和右孩子的索引。

# 测试
one_array = [5, 1, 4, 6, 4, 2, 3, 9, 1]


#        5
#       /  \
#      1    4
#     / \  /  \
#    6   4 2   3
#   / \
#  9   1


def max_heap(some_array):
    length = len(some_array)

    # 从最后一个非叶子节点开始
    for i in range(math.floor((length - 2) / 2), -1, -1):
        heapify_down(some_array, i, length)

    return some_array


def heapify_down(heap, index, heap_size):
    largest = index
    left_child = 2 * index + 1
    right_child = 2 * index + 2

    # 检查左孩子是否存在并且是否比当前节点大
    if left_child < heap_size and heap[left_child] > heap[largest]:
        largest = left_child

    # 检查右孩子是否存在并且是否比当前节点大
    if right_child < heap_size and heap[right_child] > heap[largest]:
        largest = right_child

    # 如果最大的节点不是当前节点，则交换
    if largest != index:
        heap[index], heap[largest] = heap[largest], heap[index]
        # 递归地向下调整子树
        heapify_down(heap, largest, heap_size)


print(max_heap(one_array))
