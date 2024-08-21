import tree_traversal as tree

ooe_node = tree.TreeNode(4)
two_node = tree.TreeNode(2)
three_node = tree.TreeNode(6)
four_node = tree.TreeNode(1)
five_node = tree.TreeNode(3)
six_node = tree.TreeNode(5)
seven_node = tree.TreeNode(7)
ooe_node.left = two_node
ooe_node.right = three_node
two_node.left = four_node
two_node.right = five_node
three_node.left = six_node
three_node.right = seven_node


# 判断是否为搜索二叉树
# 即左节点小于 根节点 右节点大于根节点
#   5
#  / \
# 2   7
def check_if_bst(root):
    #  中序遍历
    prev = None
    if not root:
        return True
    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        # 比较当前节点和前一个节点
        if prev is not None and current.value <= prev:
            return False

        prev = current.value  # 更新前一个节点的值
        current = current.right

    return True


print(check_if_bst(ooe_node))
