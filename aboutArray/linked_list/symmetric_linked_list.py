import linked_list

one_list = linked_list.LinkedList()
one_list.prepend(1)
one_list.append(2)
one_list.append(3)
one_list.append(4)
one_list.append(3)
one_list.append(2)
one_list.append(1)

one_list.print_list()


def speed_pointer(some_list):
    quick = 1
    slow = 1
    next_node = some_list.head
    while next_node:
        if next_node.next is not None:
            quick += 1
            slow += 0.5
        next_node = next_node.next
    return quick, slow


def check_symmetric_linked_list(some_list):
    data = speed_pointer(some_list)
    if data is False:
        return data

    quick = data[1]
    slow = data[2]




print(speed_pointer(one_list))
