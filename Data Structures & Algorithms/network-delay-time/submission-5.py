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
# 中文思路清单（Dijkstra：最小堆 + visited）
#
# 1. 明确题目目标。
#    - 从起点 k 发出信号，求所有节点都收到信号所需的最少时间。
#    - 信号可以同时沿不同路线传播。
#    - 先确定每个节点最早收到信号的时间，再取其中最大的时间。
#    - 如果有任何节点无法到达，返回 -1。
#    - 所有边的耗时都非负，因此可以使用 Dijkstra 算法。
#
# 2. 建立有向图的邻接表。
#    - graph = defaultdict(list)。
#    - 遍历 times，把每条边拆成 u、v、travel_time。
#    - graph[u].append((v, travel_time))。
#    - graph[u] 保存从 u 出发可以到达的邻居，以及每条边的耗时。
#    - 这是有向图，只添加 u 到 v，不添加反方向。
#    - 没有出边的节点，访问 graph[node] 时会得到空列表。
#
# 3. 初始化最小堆、visited 和 total_time。
#    - min_heap = [(0, k)]。
#    - 堆中保存：(从起点出发的累计时间, 到达的节点)。
#    - 起点 k 在时间 0 就有信号，所以先加入 (0, k)。
#    - 注意外层需要列表 []，因为 heapq 操作的是列表。
#    - visited = set()：保存已经确定最短到达时间的节点。
#    - total_time = 0：记录最近一个新处理的节点的最短到达时间。
#
# 4. 只要堆不为空，就继续处理候选方案。
#    - while min_heap。
#    - elapsed, node = heapq.heappop(min_heap)。
#    - 每次取出并删除累计时间最小的方案。
#    - elapsed：这条路线从起点到 node 的累计耗时。
#    - node：这条路线到达的节点。
#    - 时间相同时，Python 会继续比较节点编号，但不影响答案。
#
# 5. 如果当前节点已经处理过，跳过当前方案。
#    - if node in visited: continue。
#    - 同一个节点可能通过不同路线，多次加入堆。
#    - 第一次出堆时，它的最短到达时间已经确定。
#    - 后面再取出同一节点，就不需要重复处理。
#    - continue 只跳过当前这一轮，接着取堆中的下一个方案。
#
# 6. 确定当前节点的最短到达时间。
#    - visited.add(node)。
#    - 必须在出堆后标记，不能第一次入堆时就标记。
#    - 因为先发现的路线不一定最快。
#    - 最小堆优先处理累计时间更小的路线，且边的耗时非负，
#      因此节点第一次出堆时，不会再有更短的路线等待发现。
#    - 执行 total_time = elapsed，记录这个节点收到信号的时间。
#    - 有效处理的到达时间不会减小，允许出现相等的时间。
#    - 所以最后记录的 total_time，就是最晚收到信号的时间。
#    - 不需要累加 elapsed，也不需要额外取最大值。
#
# 7. 检查当前节点的所有邻居。
#    - for neighbor, travel_time in graph[node]。
#    - neighbor：准备到达的邻居节点。
#    - travel_time：从当前节点到这个邻居，只走这一条边的耗时。
#    - 如果 neighbor 已经在 visited 中，直接跳过这个邻居。
#    - 否则，把 (elapsed + travel_time, neighbor) 加入最小堆。
#    - elapsed + travel_time：经过当前节点，到达邻居的累计耗时。
#    - 加入堆表示发现了一条候选路线，不代表立即处理这个邻居。
#    - 之后仍然按照累计时间从小到大的顺序取出方案。
#
# 8. 堆为空时，检查是否到达全部节点。
#    - 堆为空，说明所有候选方案都已经处理完。
#    - 如果 len(visited) == n，说明全部节点都收到信号。
#    - 返回 total_time，也就是最后一个节点最早收到信号的时间。
#    - 否则，有节点无法从 k 到达，返回 -1。
#    - 起点本身也算一个节点，会在处理 (0, k) 时加入 visited。
#
# 9. 容易混淆的地方。
#    - graph 中保存 (邻居, 单条边的耗时)。
#    - min_heap 中保存 (累计时间, 到达的节点)。
#    - 入堆时第二项必须是 neighbor，不能写成当前节点 node。
#    - visited 表示“最短到达时间已经确定”，不是“曾经加入过堆”。
#    - 重复节点会在更新 total_time 之前被跳过，不会把答案改大。
#    - total_time = elapsed，不能写成 total_time += elapsed。
#    - n 是节点数，len(times) 是边数，两者不一定相等。
#
# 10. 时间和空间复杂度。
#     - 设节点数为 n，边数为 E。
#     - 每个节点最多有效处理一次，它的出边也只会遍历一次。
#     - 每条边最多产生一次入堆操作，堆中可能保留同一节点的多个方案。
#     - 时间复杂度：O(n + E * log(E + 1))。
#     - 空间复杂度：O(n + E)。
#     - 空间用于邻接表、visited 和最小堆。
#
# 快速记忆思路
# 建有向图，起点以时间 0 入堆。
# 每次取最早方案：处理过就跳过，没处理过就确定时间。
# 到邻居的时间 = 当前累计时间 + 这条边的耗时。
# 把新方案入堆，直到堆为空。
# 全部到达，返回最后的时间；有节点到不了，返回 -1。
#
# 口语讲述思路
#
# I'll use Dijkstra's algorithm because all edge weights are nonnegative.
# First, I build an adjacency list for the directed graph.
#
# I use a min-heap to store the total travel time and the node.
# I start with the source node at time zero.
# I also use a visited set to track nodes whose shortest times are finalized.
#
# Each time, I pop the entry with the smallest total time.
# If the node is already visited, I skip it.
# Otherwise, this is the shortest time to reach that node.
# I mark it as visited and record its arrival time.
#
# Then I check its outgoing edges.
# For each unvisited neighbor, I add the edge's travel time to the current time
# and push that new entry into the heap.
#
# Since the arrival times are processed in nondecreasing order,
# the last newly visited node gives us the total delay.
#
# If all n nodes are visited, I return that time.
# Otherwise, some nodes are unreachable, so I return negative one.
#
# Let E be the number of edges.
# The time complexity is O(n + E log(E + 1)).
# The space complexity is O(n + E).               

# 建图：       O(E)
# 节点处理：   O(n)
# 检查出边：   O(E)
# 堆操作：     O(E log(E + 1))
# O(E) 次堆操作 × 每次 O(log(E + 1))
# = O(E log(E + 1))
#
# 合并：
# O(n + E + E log(E + 1))
# = O(n + E log(E + 1))
                