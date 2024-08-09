# 【题目】给定一个单链表的头节点head，节点的值类型是整型，再给定一个整数pivot。
#  实现一个调整链表的函数，将链表调整为左部分都是值小于pivot的节点，中间部分都是值等于pivot的节点，右部分都是值大于pivot的节点。
# 【进阶】在实现原问题功能的基础上增加如下的要求
# 【要求】调整后所有小于pivot的节点之间的相对顺序和调整前一样
# 【要求】调整后所有等于pivot的节点之间的相对顺序和调整前一样
# 【要求】调整后所有大于pivot的节点之间的相对顺序和调整前一样
# 【要求】时间复杂度请达到O(N)，额外空间复杂度请达到O(1)。
import random

import linked_list


def partition_linked_list(head, pivot):
    # 定义三个区域的头尾节点
    small_head = small_tail = None
    equal_head = equal_tail = None
    large_head = large_tail = None

    current = head

    # 遍历链表并分区
    while current:
        next_node = current.next  # 暂存下一节点
        current.next = None  # 断开当前节点的连接

        if current.data < pivot:
            if not small_head:  # 如果小于区为空，初始化它
                small_head = small_tail = current
            else:
                small_tail.next = current
                small_tail = current
        elif current.data == pivot:
            if not equal_head:  # 如果等于区为空，初始化它
                equal_head = equal_tail = current
            else:
                equal_tail.next = current
                equal_tail = current
        else:
            if not large_head:  # 如果大于区为空，初始化它
                large_head = large_tail = current
            else:
                large_tail.next = current
                large_tail = current

        current = next_node

    # 连接三部分
    if small_tail:
        small_tail.next = equal_head if equal_head else large_head
    if equal_tail:
        equal_tail.next = large_head

    # 返回新的头节点
    return small_head if small_head else (equal_head if equal_head else large_head)


# 测试
one_list = linked_list.LinkedList()
one_list.append(3)
one_list.append(5)
one_list.append(8)
one_list.append(5)
one_list.append(10)
one_list.append(2)
one_list.append(1)

print("Original List:")
one_list.print_list()

pivot = 5
one_list.head = partition_linked_list(one_list.head, pivot)

print(f"Partitioned List around pivot {pivot}:")
one_list.print_list()