class Node:
    def __init__(self, value):
        self.value = value
        self.inside = 0
        self.outside = 0
        self.nexts = []
        self.edges = []

    def add_edges(self, node):
        self.nexts.append(node)

    def add_nexts(self, edge):
        self.edges.append(edge)


class Edge:

    def __init__(self, weight, from_node, to_node):
        self.weight = weight
        self.from_node = from_node
        self.to_node = to_node


class Graph:

    def __init__(self):
        self.nodes = {}
        self.edges = set()


def create_graph(matrix):
    graph = Graph()

    for i in range(len(matrix)):
        from_node_value = matrix[i][0]
        to_node_value = matrix[i][1]
        weight = matrix[i][2]

        # 确保节点存在
        if from_node_value not in graph.nodes:
            graph.nodes[from_node_value] = Node(from_node_value)
        if to_node_value not in graph.nodes:
            graph.nodes[to_node_value] = Node(to_node_value)

        node_from = graph.nodes[from_node_value]
        node_to = graph.nodes[to_node_value]

        new_edge = Edge(weight, node_from, node_to)

        node_from.add_edges(node_to)  # 使用已定义的方法
        node_from.outside += 1
        node_to.inside += 1

        node_from.add_nexts(new_edge)  # 使用已定义的方法
        graph.edges.add(new_edge)

    return graph


# 示例矩阵
node_matrix = [
    [1, 2, 10],
    [2, 3, 20],
    [3, 1, 15]
]

# 创建图
one_graph = create_graph(node_matrix)

# 输出节点信息
for node_value, node in one_graph.nodes.items():
    print(f"Node {node_value}: Inside Edges = {node.inside}, Outside Edges = {node.outside}")

for edge in one_graph.edges:
    print(f"Node{edge.from_node.value} to Node{edge.to_node.value}, weight = {edge.weight}")
