import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            distance_squared = x ** 2 + y ** 2
            heap.append([distance_squared, x, y])
        heapq.heapify(heap)
        result = []
        for _ in range(k):
            distance_squared, x, y = heapq.heappop(heap)
            result.append([x, y])

        return result    

#python中^2不是平方， 是**2