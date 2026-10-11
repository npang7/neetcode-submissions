import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 保存重量的负数，用最小堆取出最重的石头
        heap = []
        for weight in stones:
            heap.append(-weight)

        # 将列表转换成最小堆
        heapq.heapify(heap)

        # 至少有两块石头时，继续相撞
        while len(heap) > 1:
            # 取出最重的石头，并还原成正数
            heaviest = -heapq.heappop(heap)

            # 取出第二重的石头，并还原成正数
            second_heaviest = -heapq.heappop(heap)

            # 如果重量不同，再放回重量差对应的新石头
            if heaviest > second_heaviest:
                remaining_weight = heaviest - second_heaviest
                heapq.heappush(heap, -remaining_weight)

        # 如果还有一块石头，返回它的实际重量
        if heap:
            return -heap[0]

        # 如果没有石头，返回 0
        return 0