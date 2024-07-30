#  插入元素和删除最高优先级的元素。在许多情况下，优先队列可以通过大根堆来实现，因为大根堆能够有效地支持这两种操作。


import math


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def delete_max(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")

        # 交换最大元素（堆顶）与最后一个元素
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        # 删除最后一个元素（原来的最大元素）
        max_value = self.heap.pop()
        # 调整堆以保持堆性质
        self.heapify_down(0)
        return max_value

    def heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = (index - 1) // 2

    def heapify_down(self, index):
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child

        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)

    def __str__(self):
        return str(self.heap)


if __name__ == "__main__":
    pq = PriorityQueue()

    while True:
        action = input("Enter an action (insert/delete_max/exit): ")
        if action == "insert":
            value = int(input("Enter the value to insert: "))
            pq.insert(value)
            print("Current priority queue:", pq)
        elif action == "delete_max":
            if pq.is_empty():
                print("Priority queue is empty")
            else:
                max_value = pq.delete_max()
                print("Deleted max value:", max_value)
                print("Current priority queue:", pq)
        elif action == "exit":
            break
        else:
            print("Invalid action. Please enter 'insert', 'delete_max', or 'exit'.")
