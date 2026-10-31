class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            while len(heap) > k:
                heapq.heappop(heap)
        
        res= []
        for c , num in heap:
            res.append(num)
        return res
