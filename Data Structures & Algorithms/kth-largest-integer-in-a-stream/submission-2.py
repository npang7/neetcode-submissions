import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []

        # 处理最开始的数字
        for num in nums:
            heapq.heappush(self.min_heap, num)
            # 超过 k 个，就删除最小的数字
            # 这样留下的就是目前最大的 k 个数
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # 加入新数字
        heapq.heappush(self.min_heap, val)
        # 如果超过 k 个，删除其中最小的数字
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        # 最大的 k 个数中，最小的就是第 k 大
        return self.min_heap[0]