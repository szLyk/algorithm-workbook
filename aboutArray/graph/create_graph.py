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

    def get_edges(self):
        return self.edges


class Edge:

    def __init__(self, weight, from_node, to_node):
        self.weight = weight
        self.from_node = from_node
        self.to_node = to_node

    # 在您提供的代码中，heapq.heappush() 接收的是一个元组 (next_edge.weight, next_edge)。这里的关键是元组的第一个元素 next_edge.weight
    # 是一个数值类型（如整数或浮点数），是可以进行比较的。然而，当您尝试将整个元组加入堆时， Python 默认会首先比较元组的第一个元素（即边的权重），如果第一个元素相同，则会继续比较元组的第二个元素（即 Edge 对象）。
    # 问题出现在元组的第二个元素上，即 Edge 对象。默认情况下，Edge 类型的对象之间是没有定义如何进行比较的。因此，当第一个元素（权重）相等时，Python 试图比较 Edge 对象本身，这就触发了
    # TypeError，因为 Python 不知道如何比较两个 Edge 实例。 为了解决这个问题，我们已经在 Edge 类中实现了 __lt__ 方法来定义如何比较两个 Edge 实例。这样，即使权重相同，Python
    # 也知道如何确定哪个 Edge 实例应该排在前面。
    def __lt__(self, other):
        return self.weight < other.weight


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

        # 创建无向边
        new_edge = Edge(weight, node_from, node_to)

        # 添加节点间的连接（无向图：相互连接）
        node_from.add_nexts(node_to)
        node_to.add_nexts(node_from)

        # 增加每个节点的入度和出度
        node_from.outside += 1
        node_to.outside += 1
        node_from.inside += 1
        node_to.inside += 1

        # 添加边到每个节点（无向边）
        node_from.add_edges(Edge(weight, node_from, node_to))
        node_to.add_edges(Edge(weight, node_to, node_from))

        # 添加边到图
        graph.edges.add(new_edge)

    return graph


def print_nodes(graph):
    for node_value, node in graph.nodes.items():
        print(f"Node {node_value}: Inside Edges = {node.inside}, Outside Edges = {node.outside}")


def print_edges(graph):
    for edge in graph.edges:
        print(f"Node{edge.from_node.value} to Node{edge.to_node.value}, weight = {edge.weight}")
