# 金块切割问题
# 假设有一块黄金重为 n，需要将其切割成 m 块。每一次切割黄金都会产生成本，成本等于黄金的重量。我们需要找到一种切割顺序，使得总的切割成本最小。
# 动态规划问题 贪心算法
# 问题示例
# 假设有一个重 100 克的金块，要求将其切割成 25g, 25g, 25g, 25g 的四块。每次切割时，切割的成本等于切割时所剩下金块的重量。
# 例子 1
# 第一次切割成 75g 和 25g，成本是 100g。
# 第二次切割 75g 中的 50g 和 25g，成本是 75g。
# 第三次切割 50g 中的 25g 和 25g，成本是 50g。
# 总的切割成本为： 100 + 75 + 50 = 225g。
#
# 例子 2（不同顺序）
# 如果在开始时直接切割成 50g 和 50g：
#
# 第一次切割成 50g 和 50g，成本是 100g。
# 第二次切割 50g 中的 25g 和 25g，成本是 50g。
# 第三次切割另一个 50g，同样的成本是 50g。
# 总的切割成本为：100 + 50 + 50 = 200g。
import heapq


def cut_gold(prices):
    heapq.heapify(prices)
    total_cost = 0

    while len(prices) > 1:
        first = heapq.heappop(prices)
        second = heapq.heappop(prices)

        cost = first + second
        total_cost += cost

        heapq.heappush(prices, cost)

    return total_cost


print(cut_gold([25, 25, 25, 25]))
