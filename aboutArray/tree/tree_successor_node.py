class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


ooe_node = TreeNode(4)
two_node = TreeNode(2)
two_node.parent = ooe_node
three_node = TreeNode(6)
three_node.parent = ooe_node
four_node = TreeNode(1)
four_node.parent = two_node
five_node = TreeNode(3)
five_node.parent = two_node
six_node = TreeNode(5)
six_node.parent = three_node
seven_node = TreeNode(7)
seven_node.parent = three_node
ooe_node.left = two_node
ooe_node.right = three_node
two_node.left = four_node
two_node.right = five_node
three_node.left = six_node
three_node.right = seven_node


# 寻找某个节点的后续节点
# 按照中序遍历 后一个节点是前一个节点的后继节点
# 只给一个在二叉树中的某个节点node，请实现返回node的后继节点的函数
def find_successor(node):
    if not node.parent:
        return node

    if node.right:
        current = node.right
        while current.left:
            current = current.left
        return current
    else:
        parent = node.parent
        while node and node == parent.right:
            node = node.parent
            parent = parent.parent
        return parent


print(find_successor(six_node).value)
