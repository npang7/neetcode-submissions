import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u , v, travel_time in times:
            graph[u].append((v,travel_time))
        min_heap = [(0, k)]  #不要忘记【】！！
        total_time = 0
        visited = set()

        while min_heap:
            elapsed, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            total_time = elapsed

            for neighbor, travel_time in graph[node]:
                if neighbor in visited:
                    continue
                heapq.heappush(min_heap,
                    (total_time+travel_time,neighbor))
        if len(visited) == n:
            return total_time
        return -1
                    
                