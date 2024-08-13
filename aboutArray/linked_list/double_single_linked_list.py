#  双单链表问题 判断两个链表是否相交
import circular_linked_list as circular_list
import linked_list

one_head = linked_list.Node(1)
one_node_one = linked_list.Node(5)
one_node_two = linked_list.Node(6)
one_node_three = linked_list.Node(8)
one_node_four = linked_list.Node(4)
one_node_five = linked_list.Node(2)
one_node_six = linked_list.Node(3)
one_node_seven = linked_list.Node(9)
one_node_eight = linked_list.Node(10)
one_node_nine = linked_list.Node(11)

one_head.next = one_node_one
one_node_one.next = one_node_two
one_node_two.next = one_node_three
one_node_three.next = one_node_four
one_node_four.next = one_node_five
one_node_five.next = one_node_six
one_node_six.next = one_node_seven
one_node_seven.next = one_node_eight

two_head = linked_list.Node(1)
two_node_one = linked_list.Node(5)
two_node_two = linked_list.Node(6)
two_node_three = linked_list.Node(8)
two_node_four = linked_list.Node(4)
two_node_five = linked_list.Node(2)
two_node_six = linked_list.Node(3)
two_node_seven = linked_list.Node(9)

two_head.next = two_node_one
two_node_one.next = two_node_two
two_node_two.next = two_node_three
two_node_three.next = two_node_four
two_node_four.next = two_node_five
two_node_five.next = two_node_six
two_node_six.next = two_node_seven
two_node_seven.next = two_node_five


def judge_linked_list_intersected(first_head, second_head):
    #  先判断有没有环形节点
    first_circular = circular_list.get_circular_linked_list_node(first_head)
    second_circular = circular_list.get_circular_linked_list_node(second_head)

    if not first_circular and not second_circular:

        #  先算两个表的长度
        long_head = first_head
        short_head = second_head
        n = 0
        while first_head:
            n += 1
            first_head = first_head.next

        while second_head:
            n -= 1
            second_head = second_head.next

        if n < 0:
            long_head = second_head
            short_head = first_head

        if n < 0:
            n = -n

        while n > 0:
            long_head = long_head.next
            n -= 1

        while (long_head and short_head) and long_head != short_head:
            long_head = long_head.next
            short_head = short_head.next

        if long_head == short_head and (long_head and short_head):
            return True
        else:
            return False

    elif first_circular and second_circular:
        if first_circular == second_circular:
            return True
        else:
            tmp_node = first_circular
            first_circular = first_circular.next
            while first_circular != tmp_node:
                if first_circular == second_circular:
                    return True
                else:
                    first_circular = first_circular.next
    else:
        return False


judge_linked_list_intersected(one_head, two_head)
