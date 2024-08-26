class Node:
    def __init__(self, value):
        self.value = value
        self.inside = 0
        self.outside = 0
        self.nexts = []
        self.edges = []

    def add_nexts(self, node):
        self.nexts.append(node)

    def add_edges(self, edge):
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


def create_directed_graph(matrix):
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

        node_from.add_nexts(node_to)  # 使用已定义的方法
        node_from.outside += 1
        node_to.inside += 1

        node_from.add_edges(new_edge)  # 使用已定义的方法
        graph.edges.add(new_edge)

    return graph


def create_undirected_graph(matrix):
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

        # 创建边
        new_edge = Edge(weight, node_from, node_to)

        # 添加单向连接（双向图）
        node_from.add_nexts(node_to)
        node_to.add_nexts(node_from)

        # 增加入度和出度
        node_from.outside += 1
        node_to.outside += 1
        node_from.inside += 1
        node_to.inside += 1

        # 添加边到每个节点
        node_from.add_edges(new_edge)
        node_to.add_edges(new_edge)

        # 添加边到图
        graph.edges.add(new_edge)

    return graph


def print_nodes(graph):
    for node_value, node in graph.nodes.items():
        print(f"Node {node_value}: Inside Edges = {node.inside}, Outside Edges = {node.outside}")


def print_edges(graph):
    for edge in graph.edges:
        print(f"Node{edge.from_node.value} to Node{edge.to_node.value}, weight = {edge.weight}")
