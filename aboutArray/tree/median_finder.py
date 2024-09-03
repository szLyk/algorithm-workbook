import heapq

# 算法思想：
#
# 最大堆 (low) 存储较小的一半数值。
# 最小堆 (high) 存储较大的一半数值。
# 维护这两个堆的大小差不超过 1，以确保可以快速得到中位数。
# 对于每一个新元素：
#
# 如果新元素比最大堆的堆顶大，放入最小堆；
# 否则，放入最大堆。
# 然后调整两个堆的大小平衡，使得两堆的大小差保持在 1 以内。
# 最终：
#
# 如果两个堆的大小相等，中位数是两堆堆顶元素的平均值。
# 如果两个堆的大小不等，中位数是较大堆的堆顶元素。

class MedianFinder:
    def __init__(self):
        # 最大堆 (使用负数来实现最大堆)
        self.low = []
        # 最小堆
        self.high = []

    def add_num(self, num):
        # 首先将 num 添加到最大堆（low）
        heapq.heappush(self.low, -num)

        # 确保最大堆的最大值 <= 最小堆的最小值
        if self.low and self.high and (-self.low[0] > self.high[0]):
            # 将最大堆的最大值移动到最小堆中
            val = -heapq.heappop(self.low)
            heapq.heappush(self.high, val)

        # 平衡两个堆的大小，使最大堆的元素个数 ≥ 最小堆
        if len(self.low) > len(self.high) + 1:
            val = -heapq.heappop(self.low)
            heapq.heappush(self.high, val)
        elif len(self.high) > len(self.low):
            val = heapq.heappop(self.high)
            heapq.heappush(self.low, -val)

    def find_median(self):
        if len(self.low) > len(self.high):
            return -self.low[0]  # 最大堆的堆顶即为中位数
        return (-self.low[0] + self.high[0]) / 2  # 如果元素个数相同，返回两个堆顶元素的平均值

# 使用例子
median_finder = MedianFinder()

# 插入数据流中的数据
numbers = [5, 2, 10, 1, 3, 7, 8]
for num in numbers:
    median_finder.add_num(num)
    print(f"当前数据流: {numbers[:numbers.index(num) + 1]}")
    print(f"当前中位数: {median_finder.find_median()}")
