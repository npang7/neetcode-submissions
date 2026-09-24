class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k :
                heapq.heappop(heap)
        arr = []
        for i in range(k):
            arr.append(heapq.heappop(heap)[1])
        return arr
            
