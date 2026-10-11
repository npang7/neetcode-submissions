import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            # 加入当前数字
            heapq.heappush(heap, num)
            # 超过 k 个，就删除其中最小的数字
            # 这样保留的就是目前最大的 k 个数
            if len(heap) > k:
                heapq.heappop(heap)

        # 最大的 k 个数中，最小的就是第 k 大
        return heap[0]