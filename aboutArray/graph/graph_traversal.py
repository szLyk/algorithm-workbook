# 图的递归
# 宽度遍历 和 深度遍历
import create_graph as graph
from collections import deque


# 宽度遍历
def width_traversal(some_graph):
    nodes = some_graph.nodes
    visited = set()  # 存储已访问的节点
    result = []  # 用于存储遍历结果

    # 遍历所有的节点，防止有孤立节点未被访问
    for node in nodes.values():
        if node not in visited:
            queue = deque([node])
            visited.add(node)

            while queue:
                current_node = queue.popleft()
                result.append(current_node.value)

                # 遍历当前节点的所有邻居
                for next_node in current_node.nexts:
                    if next_node not in visited:
                        visited.add(next_node)
                        queue.append(next_node)

    return result


# 深度遍历
def depth_traversal(some_graph):
    nodes = some_graph.nodes
    visited = set()  # 存储访问过的节点
    stack = []  # 栈，用于深度优先遍历的辅助

    result = []  # 存储遍历的结果

    # 遍历每个节点，防止有孤立节点没被访问
    for node in nodes.values():
        if node not in visited:
            # DFS 从该节点开始
            stack.append(node)
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    result.append(current.value)
                    # 将邻居节点压入栈中
                    for next_node in reversed(current.nexts):  # 倒序压栈保持正确顺序
                        if next_node not in visited:
                            stack.append(next_node)

    return result


# 示例矩阵
node_matrix = [
    ['A', 'B', 10],
    ['A', 'C', 15],
    ['A', 'D', 25],
    ['B', 'E', 20],
    ['C', 'E', 30],
    ['D', 'F', 35],
    ['E', 'F', 5],
]

# 创建图
one_graph = graph.create_directed_graph(node_matrix)

# graph.print_nodes(one_graph)
# graph.print_edges(one_graph)
print(width_traversal(one_graph))
print(depth_traversal(one_graph))
