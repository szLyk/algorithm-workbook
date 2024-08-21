# 二叉树层数节点计算
from collections import deque

import tree_traversal

ooe_node = tree_traversal.TreeNode(1)
two_node = tree_traversal.TreeNode(2)
three_node = tree_traversal.TreeNode(3)
four_node = tree_traversal.TreeNode(4)
five_node = tree_traversal.TreeNode(5)
six_node = tree_traversal.TreeNode(6)
seven_node = tree_traversal.TreeNode(7)
ooe_node.left = two_node
ooe_node.right = three_node
two_node.left = four_node
two_node.right = five_node
three_node.left = six_node
three_node.right = seven_node


# 计算当前最大节点数
def max_nodes_per_level(root):
    if not root:
        return 0

    queue = deque([root])
    max_count = 0
    current_count = 0
    level_count = 0

    while queue:
        current_count = len(queue)  # 当前层的节点数
        for _ in range(current_count):
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        max_count = max(max_count, current_count)
        level_count += 1

    return max_count
