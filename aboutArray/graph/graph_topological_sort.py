#  图的拓扑排序

import create_graph as graph
from collections import deque


def topological_sort(some_graph):
    queue = deque()
    result = []

    nodes = some_graph.nodes
    hash_map = {}

    for node in nodes.values():
        in_cnt = node.inside
        hash_map[node] = in_cnt
        if in_cnt == 0:
            queue.append(node)

    # 拓扑排序
    while queue:
        current = queue.popleft()
        result.append(current.value)

        # 更新邻接节点的入度
        for next_node in current.nexts:
            hash_map[next_node] -= 1
            if hash_map[next_node] == 0:
                queue.append(next_node)

    return result


# 示例矩阵
node_matrix = [
    ['D', 'B', 10],
    ['E', 'B', 15],
    ['F', 'C', 25],
    ['B', 'A', 20],
    ['C', 'A', 30]
]

# 创建图
one_graph = graph.create_directed_graph(node_matrix)

print(topological_sort(one_graph))
