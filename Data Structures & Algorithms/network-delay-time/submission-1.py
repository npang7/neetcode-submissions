import heapq
from collections import defaultdict
class Solution: #Dijkstra's Algorithm
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # graph[u] 保存：(邻居节点, 这条边的耗时)
        graph = defaultdict(list)
        for u, v, travel_time in times:
            graph[u].append((v, travel_time))

        # 保存：(从起点出发的累计时间, 到达的节点)
        min_heap = [(0, k)]
        # 已经确定最短到达时间的节点
        visited = set()
        # 最近一个新处理的节点收到信号的时间
        total_time = 0

        while min_heap:
            #取出并删除堆中最小的元素，取出的是当前累计时间最小的方案
            elapsed, node = heapq.heappop(min_heap)

            # 同一个节点可能有多个候选方案，只处理第一次出堆的
            if node in visited:
                continue

            # 第一次出堆时，该节点的最短到达时间已经确定
            visited.add(node)
            total_time = elapsed

            for neighbor, travel_time in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap,
                        (elapsed + travel_time, neighbor))

        if len(visited) == n:
            return total_time
        else:
            return -1