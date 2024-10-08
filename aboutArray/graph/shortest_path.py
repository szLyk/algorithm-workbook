import create_graph as graph
import heapq


# 图的最短路径问题
# K算法 和 p算法
# K算法（通常指的是Kruskal算法）和P算法（通常指的是Prim算法）


# Kruskal算法 (K算法)
# Kruskal算法用于计算最小生成树，它基于“边的贪心选择策略”。通过不断选择权值最小的边，将不连通的顶点逐步连接，最终生成一个连通的无环子图，即最小生成树。
# Kruskal算法的步骤：
# 边排序：对图中所有边按权值从小到大排序。
# 并查集：使用并查集结构来跟踪节点的连接状态，防止形成环。
# 贪心选择边：从权值最小的边开始，依次选择边，如果加入该边不形成环，则将其加入最小生成树中。
# 终止条件：当树中包含n-1条边时（n为图中的顶点数），算法终止。
# Kruskal算法的优点：
# 适用于稀疏图（边数远小于顶点数）。
# 易于实现，且能通过并查集提高效率。
# 复杂度：
# 时间复杂度为 O(E log E)，E 是边的数量。
# 并查集（Disjoint Set Union - DSU）

# 并查集（Union-Find）实现
class UnionFind:
    def __init__(self, nodes):
        self.parent = {}
        #  用于标记根节点 如果存在多条不相连的边
        self.rank = {}

        for node in nodes:
            self.parent[node] = node
            self.rank[node] = 0

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # 路径压缩
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            # 按秩合并
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def kruskal(graph):
    mst = []  # 存储最小生成树的边
    uf = UnionFind(graph.nodes.values())

    # 将边按权重排序
    sorted_edges = sorted(graph.edges, key=lambda edge: edge.weight)

    # 按权重从小到大遍历边
    for edge in sorted_edges:
        if uf.find(edge.from_node) != uf.find(edge.to_node):
            uf.union(edge.from_node, edge.to_node)
            mst.append(edge)

    return mst


# Prim算法 (P算法)
# Prim算法同样用于计算最小生成树，但它基于“顶点的贪心选择策略”。它从一个起始点开始，逐步扩展已构建的最小生成树，通过选择与当前树相连的权值最小的边将新顶点加入树中。
# Prim算法的步骤：
# 初始化：选择一个任意顶点作为起始点，将其加入树中。
# 贪心选择顶点：从所有与当前树相连的边中，选择权值最小的边，并将这条边的另一个端点加入树中。
# 重复步骤2，直到所有顶点都被加入树中。
# Prim算法的优点：
# 适用于稠密图（边数接近顶点数的平方）。
# 实现相对简单，特别是对于连通图的情况。
# 复杂度：
# 时间复杂度为 O(E log V)，E 是边的数量，V 是顶点的数量。


def prim(some_graph):
    # 初始化
    visited = set()
    min_heap = []
    result = []

    # 选择一个初始节点
    start_node = next(iter(some_graph.nodes.values()))
    visited.add(start_node)

    # 将与初始节点相关的所有边加入小根堆
    for edge in start_node.edges:
        # 当权重一样时 会进行第二个参数的比较 需要对象也有比较的函数 不然就会报错
        heapq.heappush(min_heap, (edge.weight, edge))

    # Prim 算法的核心
    while min_heap:
        # 取出权值最小的边
        weight, edge = heapq.heappop(min_heap)

        # 如果该边的终点已经访问过，跳过
        if edge.to_node in visited:
            continue

        # 将该边加入结果集
        result.append(edge)
        visited.add(edge.to_node)

        # 将新节点的所有边放入堆中
        for next_edge in edge.to_node.edges:
            if next_edge.to_node not in visited:
                heapq.heappush(min_heap, (next_edge.weight, next_edge))

    return result


# Dijkstra算法：适用于加权图，可以有效计算单源点到所有其他顶点的最短路径，但不支持负权重的边。


def dijkstra(graph):
    # 初始化距离和优先队列
    nodes = graph.nodes.values()
    distances = {node: float('infinity') for node in nodes}
    one_node = next(iter(nodes))
    distances[one_node] = 0
    priority_queue = [(0, one_node)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # 跳过已访问的节点
        if current_distance > distances[current_node]:
            continue

        # 更新邻接节点的距离
        for edge in current_node.edges:
            weight = edge.weight
            to_node = edge.to_node
            distance = current_distance + weight
            if distance < distances[to_node]:
                distances[to_node] = distance
                heapq.heappush(priority_queue, (distance, to_node))

    return distances


# 示例矩阵
node_matrix = [
    ['A', 'B', 10],
    ['A', 'C', 15],
    ['A', 'D', 25],
    ['B', 'E', 20],
    ['C', 'E', 30],
    ['C', 'F', 50],
    ['D', 'B', 5],
    ['D', 'C', 25],
    ['D', 'E', 55],
    ['E', 'F', 35],

    ['X', 'Y', 40]
]

# 创建图
one_graph = graph.create_undirected_graph(node_matrix)

# result = prim(one_graph)
# while result:
#     edge = result.pop()
#     print("{} -> {}".format(edge.from_node.value, edge.to_node.value))


# result = kruskal(one_graph)
#
# while result:
#     value = result.pop()
#     print("{} -> {}".format(value.from_node.value, value.to_node.value))


result = dijkstra(one_graph)
keys = result.keys()
for key in keys:
    value = result.get(key)
    print("{} -> {}".format(key.value, value))
