import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        miniheap = []
        for weight in stones:
            miniheap.append(-weight)  #这里能用push吗
        heapq.heapify(miniheap)
        while len(miniheap) > 1:
            largest1 = -heapq.heappop(miniheap)
            largest2 = -heapq.heappop(miniheap)
            if largest1 > largest2:
                remaining = largest2 - largest1
                heapq.heappush(miniheap,remaining)
        if miniheap:
            return -miniheap[0]
        return 0