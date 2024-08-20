from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#  先序遍历
def print_preamble(node):
    if node is None:
        return
    print(node.value)
    print_preamble(node.left)
    print_preamble(node.right)


#  后序遍历
def print_subsequent(node):
    if node is None:
        return
    print_subsequent(node.left)
    print_subsequent(node.right)
    print(node.value)


#  中序遍历
def print_inorder(node):
    if node is None:
        return
    print_inorder(node.left)
    print(node.value)
    print_inorder(node.right)


def print_preamble_non_recursive(root):
    stack_one = [root]
    result = []

    while stack_one:
        current_node = stack_one.pop()
        result.append(current_node.value)
        if current_node.right:
            stack_one.append(current_node.right)
        if current_node.left:
            stack_one.append(current_node.left)
    return result


def print_inorder_non_recursive(root):
    if not root:
        return []

    stack = []
    current_node = root
    result = []

    while stack or current_node:
        # 一直深入左子树
        while current_node:
            stack.append(current_node)
            current_node = current_node.left

        # 处理节点
        current_node = stack.pop()
        result.append(current_node.value)

        # 进入右子树
        current_node = current_node.right

    return result


def print_subsequent_non_recursive(root):
    if not root:
        return

    stack = [root]
    output = []
    result = []

    while stack:
        current_node = stack.pop()
        output.append(current_node.value)

        # 先将左子节点压入栈，然后右子节点压入栈
        if current_node.left:
            stack.append(current_node.left)
        if current_node.right:
            stack.append(current_node.right)

    # 由于后序遍历是先处理子节点再处理根节点，因此需要反转结果
    while output:
        result.append(output.pop())

    return result


#  宽度遍历
def print_width_traversal(root):
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result


ooe_node = TreeNode(1)
two_node = TreeNode(2)
three_node = TreeNode(3)
four_node = TreeNode(4)
five_node = TreeNode(5)
six_node = TreeNode(6)
seven_node = TreeNode(7)
ooe_node.left = two_node
ooe_node.right = three_node
two_node.left = four_node
two_node.right = five_node
three_node.left = six_node
three_node.right = seven_node

# print_inorder(ooe_node)
# print(print_preamble_non_recursive(ooe_node))
print(print_subsequent_non_recursive(ooe_node))
