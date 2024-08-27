import create_graph as graph


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
    nodes = some_graph.nodes
    one_node = next(iter(nodes.values()))
    stack = [one_node]
    visited = set()
    result = []

    while stack:
        current = stack.pop()
        visited.add(current)
        result.append(current)
        edges = current.edges
        # 自定义排序函数
        sorted_edge = sorted(edges, key=lambda e: e.weight, reverse=True)
        while sorted_edge:
            to_node = sorted_edge.pop().to_node
            if to_node not in visited:
                stack.append(to_node)
                break
    return result


# Dijkstra算法：适用于加权图，可以有效计算单源点到所有其他顶点的最短路径，但不支持负权重的边。
# Bellman-Ford算法：可以处理负权重边，并且也能找出单源点到所有其他顶点的最短路径。
# Floyd-Warshall算法：适用于求解所有顶点对之间的最短路径，使用动态规划思想，处理负权重边但不允许负权环。
# A*算法：是一种启发式算法，通常用于路径搜索问题。

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
]

# 创建图
one_graph = graph.create_undirected_graph(node_matrix)
graph.print_edges(one_graph)
result = prim(one_graph)
while result:
    print(result.pop().value)