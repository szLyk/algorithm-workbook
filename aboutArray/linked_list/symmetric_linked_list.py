import math

import linked_list

one_list = linked_list.LinkedList()
one_list.prepend(1)
one_list.append(2)
one_list.append(3)
one_list.append(4)
one_list.append(4)
one_list.append(3)
one_list.append(2)
one_list.append(1)


def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def print_linked_list(node):
    while node:
        print(str(node.data), end=" => ")
        node = node.next
    print("None")


def check_symmetric_linked_list(some_list):
    if some_list.head is None:
        return True

    # 使用快慢指针找到链表中点
    slow = some_list.head
    fast = some_list.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 反转后半部分链表
    second_half_head = reverse_linked_list(slow)
    copy_second_half_head = second_half_head

    # 比较前半部分和反转后的后半部分
    first_half_head = some_list.head
    is_symmetric = True
    while second_half_head:
        if first_half_head.data != second_half_head.data:
            is_symmetric = False
            break
        first_half_head = first_half_head.next
        second_half_head = second_half_head.next

    # 恢复链表原始结构
    copy_second_half_head = reverse_linked_list(copy_second_half_head)

    return is_symmetric


one_list.print_list()
print(check_symmetric_linked_list(one_list))
