# 项目选择问题，你有多个项目，每个项目有一个成本和利润，并且你只能串行完成项目。初始时，你有一个启动资金，你需要选择项目来最大化最终的利润。
import heapq

def find_max_profit(initial_savings, k, arrays):
    max_profit = initial_savings
    max_projects = k

    # 最小成本堆，按成本排序
    min_cost_pro = []
    # 最大利润堆，按利润排序
    max_profit_pro = []

    # 初始化所有项目到最小成本堆
    for cost, profit in arrays:
        heapq.heappush(min_cost_pro, (cost, profit))

    # 做最多 k 个项目
    for _ in range(max_projects):
        # 将所有可以做的项目（当前资金足够）移动到最大利润堆中
        while min_cost_pro and min_cost_pro[0][0] <= max_profit:
            cost, profit = heapq.heappop(min_cost_pro)
            # 利用负数构建最大堆（因为 heapq 默认是最小堆）
            heapq.heappush(max_profit_pro, (-profit, cost))

        # 如果没有可以做的项目了，提前退出
        if not max_profit_pro:
            break

        # 做利润最高的项目，先扣除成本，再增加利润
        profit, cost = heapq.heappop(max_profit_pro)
        max_profit -= cost  # 扣除成本
        max_profit += -profit  # 加上利润

    return max_profit


projects = [(1, 3), (2, 3), (2, 4), (3, 4), (5, 7), (6, 6)]
initial_savings = 1
k = 3  # 最多做3个项目
result = find_max_profit(initial_savings, k, projects)
print(f"最终的最大资金: {result}")

