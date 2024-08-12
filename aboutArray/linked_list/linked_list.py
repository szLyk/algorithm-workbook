class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def print_list(self):
        current = self
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# 示例
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
# ll.print_list()  # 输出: 1 -> 2 -> 3 -> None

ll.prepend(0)
# ll.print_list()  # 输出: 0 -> 1 -> 2 -> 3 -> None

ll.delete_with_value(2)
# ll.print_list()  # 输出: 0 -> 1 -> 3 -> None

node = ll.find(1)
