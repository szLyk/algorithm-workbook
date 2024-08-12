import linked_list

head = linked_list.Node(1)
node_one = linked_list.Node(5)
node_two = linked_list.Node(6)
node_three = linked_list.Node(8)
node_four = linked_list.Node(4)
node_five = linked_list.Node(2)
node_six = linked_list.Node(3)
node_seven = linked_list.Node(9)

head.next = node_one
node_one.next = node_two
node_two.next = node_three
node_three.next = node_four
node_four.next = node_five
node_five.next = node_six
node_six.next = node_seven
node_seven.next = node_five


#  获取环形链表 入环节点
def get_circular_linked_list_node(current):
    fast = current.next.next
    slow = current.next

    while (fast and slow) and fast != slow:
        fast = fast.next.next
        slow = slow.next

    if not fast or not slow:
        return None

    fast = current

    while fast != slow:
        fast = fast.next
        slow = slow.next

    return fast


node = get_circular_linked_list_node(head)
if get_circular_linked_list_node(head):
    print(node.data)
else:
    print(node)
