# 测试
# 大根堆 数组未知

# 每输入一个数 最后结果是一个大根堆

import math


def max_heap_insert(heap, value):
    heap.append(value)
    heapify_up(heap, len(heap) - 1)
    return heap


def heapify_up(heap, index):
    parent = (index - 1) // 2
    while index > 0 and heap[parent] < heap[index]:
        heap[parent], heap[index] = heap[index], heap[parent]
        index = parent
        parent = (index - 1) // 2


def main():
    heap = []

    while True:
        try:
            # 接收用户输入
            value = int(input("Enter a number (or type 'exit' to finish): "))
            # 将数字加入到数组中
            heap = max_heap_insert(heap, value)
            print("Current max heap:", heap)
        except ValueError:
            # 用户输入 'exit'
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
