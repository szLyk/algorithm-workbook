# 背包问题
# 题目：0-1 背包问题
# 给定 N 件物品，每件物品都有一个重量 weight[i] 和一个价值 value[i]。现在有一个容量为 W 的背包，要求你选择一些物品装入背包，使得在不超过背包容量的前提下，选入的物品总价值最大。
# 输入
# 一个整数 N 表示物品的数量。
# 一个整数 W 表示背包的容量。
# 两个列表：weight[] 表示每件物品的重量，value[] 表示每件物品的价值。
# 输出
# 返回在不超过背包容量的情况下，能够获得的最大总价值。

# N = 4, W = 7
# weight = [1, 3, 4, 5]
# value = [1, 4, 5, 7]

def knapsack(weights_and_values, capacity):
    n = len(weights_values)
    # 创建一个二维数组来存储子问题的解
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # 填充 dp 数组
    for i in range(1, n + 1):
        weight, value = weights_values[i - 1]  # 获取当前物品的重量和价值
        for w in range(capacity + 1):
            if weight > w:
                # 如果当前物品的重量超过了背包容量，则不选择该物品
                dp[i][w] = dp[i - 1][w]
            else:
                # 否则，选择或不选择当前物品
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

    return dp[n][capacity]


# 示例使用
weights_values = [(2, 3), (3, 4), (4, 5), (5, 6)]
capacity = 8
max_value = knapsack(weights_values, capacity)
print(f"The maximum value that can be obtained is {max_value}.")
