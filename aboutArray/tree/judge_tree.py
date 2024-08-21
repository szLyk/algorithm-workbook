import tree_traversal as tree
import math
from collections import deque

ooe_node = tree.TreeNode(5)
two_node = tree.TreeNode(3)
three_node = tree.TreeNode(7)
four_node = tree.TreeNode(2)
five_node = tree.TreeNode(4)
six_node = tree.TreeNode(6)
seven_node = tree.TreeNode(7)
ooe_node.left = two_node
ooe_node.right = three_node
two_node.left = four_node
two_node.right = five_node
three_node.left = six_node
four_node.left = seven_node


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


# 判断是否为搜索二叉树 用递归的形式
def check_if_bst_recursive(node, min_val=-math.inf, max_val=math.inf):
    # 如果当前节点为空，返回True
    if node is None:
        return True

    # 如果当前节点不在[min_val, max_val]区间内，返回False
    if not (min_val < node.value < max_val):
        return False

    # 递归检查左子树，更新上界为当前节点的值
    is_left_bst = check_if_bst_recursive(node.left, min_val, node.value)

    # 递归检查右子树，更新下界为当前节点的值
    is_right_bst = check_if_bst_recursive(node.right, node.value, max_val)

    # 当前节点的左右子树都满足条件时，才是BST
    return is_left_bst and is_right_bst


# 判断是否为完全二叉树 一个方法 两个条件
# 方法： 需要进行层数遍历
# 第一个条件： 如果一个根节点只有右节点没有左节点 那就不为二叉树
# 第二个条件： 在第一个条件满足的条件下 如果是有一个左节点 那么当出现一个没有右节点的节点时 剩下的每一层数据必须是满左右两个节点
def if_complete_binary_tree(root):
    if not root:
        return True

    queue = deque([root])
    encountered_empty = False  # 标志是否遇到空节点

    while queue:
        current = queue.popleft()

        # 左子树
        if current.left:
            if encountered_empty:
                return False
            queue.append(current.left)
        else:
            encountered_empty = True

        # 右子树
        if current.right:
            if encountered_empty:
                return False
            queue.append(current.right)
        else:
            encountered_empty = True

    return True


print(if_complete_binary_tree(ooe_node))
