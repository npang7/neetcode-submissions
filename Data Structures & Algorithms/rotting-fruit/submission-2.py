from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh = 0
        minutes = 0
        # 收集所有腐烂水果，并统计新鲜水果
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(-1, 0),(1, 0),(0, -1),(0, 1) ]
        while queue and fresh > 0:
            # 固定这一层的数量，代表本分钟负责传播的水果
            level_size = len(queue)

            for _ in range(level_size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if grid[nr][nc] != 1:
                        continue   # 只处理新鲜水果, 0/2跳过

                    # 新鲜水果变腐烂，并加入下一层
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))

            minutes += 1 # 当前这一层处理完，经过了一分钟

        if fresh > 0:
            return -1

        return minutes
# 中文思路清单（多源 BFS：每一层代表一分钟）
#
# 1. 初始化关键变量。
#    - rows、cols：网格的行数和列数。
#    - queue：保存等待向邻居传播腐烂的水果坐标。
#    - fresh = 0：剩余的新鲜水果数量。
#    - minutes = 0：已经经过的分钟数。
#    - 格子的值：0 是空格子，1 是新鲜水果，2 是腐烂水果。
#
# 2. 遍历网格，收集起点并统计新鲜水果。
#    - 遇到 2：把坐标 (r, c) 加入队列。
#    - 遇到 1：执行 fresh += 1。
#    - 所有初始腐烂水果都先入队，再开始 BFS。
#    - 这是多源 BFS，因为腐烂可以从多个起点一起传播。
#
# 3. 定义上下左右四个方向。
#    - (-1, 0)：上；(1, 0)：下。
#    - (0, -1)：左；(0, 1)：右。
#    - dr、dc 表示行号和列号的变化。
#    - 只能通过相邻水果传播，不能跨过空格子或者沿对角线传播。
#
# 4. 当 queue 不为空，并且 fresh > 0 时，继续 BFS。
#    - queue 不为空：还有水果可以尝试向周围传播。
#    - fresh > 0：还有新鲜水果需要腐烂。
#    - 两个条件同时满足，才需要继续处理下一分钟。
#    - 如果新鲜水果已经全部腐烂，立即停止，避免多算一分钟。
#
# 5. 在每轮开始时，固定当前层的水果数量。
#    - level_size = len(queue)。
#    - 这一层是本分钟负责传播的腐烂水果。
#    - 使用 for _ in range(level_size)，只处理这一层。
#    - 本轮新加入的水果留到下一轮，不能在同一分钟继续传播。
#
# 6. 在本层的 for 循环里面，逐个取出水果并检查邻居。
#    - r, c = queue.popleft()：取出一个本层水果。
#    - popleft() 必须放在本层 for 循环内部。
#    - nr = r + dr，nc = c + dc：计算邻居坐标。
#    - 如果 nr < 0 或 nr >= rows，跳过。
#    - 如果 nc < 0 或 nc >= cols，跳过。
#    - 如果 grid[nr][nc] != 1，也跳过。
#    - 只处理新鲜水果，空格子和已腐烂水果都不需要处理。
#
# 7. 将相邻的新鲜水果变成腐烂水果。
#    - grid[nr][nc] = 2：标记这个水果已经腐烂。
#    - fresh -= 1：剩余新鲜水果减少一个。
#    - queue.append((nr, nc))：加入下一层，下一分钟继续传播。
#    - 先标记，再入队，避免同一个水果被重复处理。
#    - 即使多个腐烂水果都邻接它，也只减少一次 fresh。
#
# 8. 当前这一层处理完成后，增加分钟数。
#    - minutes += 1。
#    - 这行放在本层 for 循环外、while 循环内。
#    - 每处理完一整层，才代表经过一分钟。
#    - 不能每处理一个水果就增加一分钟，因为本层水果同时传播。
#
# 9. 循环结束后，根据 fresh 判断结果。
#    - 如果 fresh > 0，说明仍有水果无法腐烂，返回 -1。
#    - 否则，返回 minutes。
#    - 开始就没有新鲜水果：循环不会执行，返回 0。
#    - 有新鲜水果但没有腐烂水果：队列为空，返回 -1。
#
# 10. 容易混淆的地方。
#     - while 条件是 queue and fresh > 0，不能只检查 queue。
#       否则可能多处理最后一层，导致多算一分钟。
#     - level_size 要在本轮开始时保存，固定本轮处理数量。
#     - popleft() 在本层 for 循环里面，每次取出一个水果。
#     - 新腐烂的水果必须入队，下一轮才能继续传播。
#     - minutes += 1 在整层处理完之后执行。
#     - 把水果改成 2，也完成了已访问标记，不需要 visited 集合。
#     - BFS 按分钟逐层传播，每个水果第一次被发现时，
#       就得到了它最早能够腐烂的时间。
#     - 这种写法会修改原始 grid，但最终返回的是分钟数。
#
# 11. 时间和空间复杂度。
#     - 假设网格有 m 行、n 列。
#     - 时间复杂度：O(m * n)。
#       初始化时遍历整个网格，每个水果最多入队一次，
#       出队后只检查四个方向。
#     - 空间复杂度：O(m * n)。
#       最坏情况下，队列需要保存 O(m * n) 个坐标。
#
# 快速记忆思路
# 腐烂水果全入队，新鲜水果先计数。
# 固定一层 → 逐个出队 → 新鲜邻居变 2、数量减 1、加入下一层。
# 整层结束加一分钟；最后有新鲜水果就返回 -1，否则返回分钟数。
#
# 口语讲述思路
#
# I'll use multi-source BFS because all rotten fruits spread at the same time.
#
# First, I scan the grid, add all initially rotten fruits to a queue,
# and count the fresh fruits.
#
# While the queue is not empty and there are still fresh fruits,
# I process one BFS layer.
# At the start of each layer, I save the current queue size
# so that newly rotten fruits are processed in the next minute.
#
# For each fruit in the current layer, I remove it from the front
# and check its four neighbors.
# I skip positions that are out of bounds or don't contain fresh fruit.
#
# When I find a fresh neighbor, I change it to two,
# decrease the fresh fruit count, and add its position to the queue.
# Marking it immediately prevents duplicate processing.
#
# After processing the entire layer, I increase the minute count by one.
# I stop once there are no fresh fruits left, so I don't count an extra minute.
#
# If fresh fruits remain after the queue becomes empty, I return minus one.
# Otherwise, I return the number of minutes.
# If there were no fresh fruits initially, the result is zero.
#
# The time complexity is O(m * n), where m and n are the grid dimensions.
# The space complexity is also O(m * n) in the worst case for the queue.