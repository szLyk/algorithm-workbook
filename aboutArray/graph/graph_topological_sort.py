#  图的拓扑排序

import create_graph as graph


def topological_sort(some_graph):
    nodes = some_graph.nodes
    items = nodes.values

    hash_set = set()



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

graph.print_edges(one_graph)
