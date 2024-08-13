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

    result = []
    stack = []
    current = root
    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            result.append(current.value)
            current = current.right

    return result


def print_subsequent_non_recursive(root):
    if not root:
        return []

    stack = []
    result = []
    current = root
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            result.append(current.value)
            current = current.right


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
print(print_inorder_non_recursive(ooe_node))
