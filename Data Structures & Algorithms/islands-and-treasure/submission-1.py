from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647

        queue = deque()
        # 把所有宝箱加入队列，作为 BFS 的起点
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]

        while queue:
            # 取出最早加入队列的格子
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                # 邻居越界，跳过
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                # 只处理尚未访问的陆地
                if grid[nr][nc] != INF:
                    continue

                # 邻居距离 = 当前距离 + 1
                grid[nr][nc] = grid[r][c] + 1
                # 之后继续从这个邻居向外搜索
                queue.append((nr, nc))

#为什么第一次填写的距离一定最短？
# 因为队列保证了：
# 先处理距离 0 的格子，再处理距离 1 的格子，再处理距离 2 的格子……
# 因此，一块陆地第一次被发现时，已经是从所有宝箱出发能到达它的最少步数。  

# 中文思路清单（多源 BFS：从所有宝箱出发，填写最短距离）
#
# 1. 检查网格是否为空。
#    - 如果 grid 为空，或者第一行没有格子，直接结束函数。
#    - 题目要求原地修改 grid，不需要返回新的网格。
#
# 2. 初始化关键变量。
#    - rows = len(grid)：网格的行数。
#    - cols = len(grid[0])：网格的列数。
#    - INF = 2147483647：表示尚未填写距离的陆地。
#    - queue = deque()：保存等待检查邻居的格子坐标。
#    - 队列只存坐标，距离直接保存在 grid 中。
#
# 3. 遍历整个网格，把所有宝箱加入队列。
#    - 如果 grid[r][c] == 0，就加入坐标 (r, c)。
#    - 所有宝箱到自己的距离都是 0。
#    - 必须先收集所有宝箱，再开始 BFS。
#    - 多源 BFS 就是从多个起点出发，在同一次 BFS 中搜索。
#
# 4. 定义上下左右四个方向。
#    - (-1, 0)：上。
#    - (1, 0)：下。
#    - (0, -1)：左。
#    - (0, 1)：右。
#    - dr 表示行号变化，dc 表示列号变化。
#
# 5. 只要队列不为空，就取出一个格子。
#    - r, c = queue.popleft()：取出最早加入的坐标。
#    - r、c 是当前格子的行号和列号。
#    - 当前格子的最短距离已经保存在 grid[r][c] 中。
#    - 使用 popleft() 保证先进先出，按照距离从小到大处理。
#
# 6. 依次检查当前格子的四个邻居。
#    - nr = r + dr：邻居的行号。
#    - nc = c + dc：邻居的列号。
#    - 如果 nr < 0 或 nr >= rows，跳过这个邻居。
#    - 如果 nc < 0 或 nc >= cols，跳过这个邻居。
#    - 先检查越界，再读取 grid[nr][nc]。
#
# 7. 只处理值仍然是 INF 的邻居。
#    - 如果 grid[nr][nc] != INF，使用 continue 跳过。
#    - -1 是水，不能经过。
#    - 0 是宝箱，已经加入过初始队列。
#    - 正整数表示已经确定距离的陆地，不需要再次访问。
#    - continue 只跳过当前邻居，接着检查下一个方向。
#
# 8. 给未访问的邻居填写距离，再加入队列。
#    - grid[nr][nc] = grid[r][c] + 1。
#    - 从当前格子走到相邻格子，需要多走一步。
#    - 修改后，邻居不再是 INF，同时完成了已访问标记。
#    - 再执行 queue.append((nr, nc))，之后从它继续向外搜索。
#    - 必须先填写距离，再入队，避免同一个格子重复入队。
#    - 不需要额外的 visited 集合。
#
# 9. 理解为什么第一次填写的距离一定最短。
#    - 所有宝箱一开始都在队列中，距离都是 0。
#    - 新发现的邻居加入队尾，不会立即继续向下搜索。
#    - 因此，所有距离为 0 的格子先处理，然后是距离 1、2、3……
#    - 离某个宝箱近的路线，会先于更远的路线到达目标格子。
#    - 第一次发现一块陆地时，得到的就是到最近宝箱的最短距离。
#    - 每次移动都算一步，这是 BFS 能保证最短距离的关键条件。
#
# 10. 队列为空时结束。
#     - 所有能从宝箱到达的陆地，都已经填写最短距离。
#     - 无法到达任何宝箱的陆地不会被访问，保留 INF。
#     - 如果没有宝箱，初始队列为空，网格保持原样。
#     - 函数默认返回 None，结果保存在原来的 grid 中。
#
# 11. 时间和空间复杂度。
#     - 假设网格有 m 行、n 列。
#     - 时间复杂度：O(m * n)。
#       初始化时遍历整个网格；每个格子最多入队一次，
#       出队后只检查四个方向。
#     - 空间复杂度：O(m * n)。
#       最坏情况下，队列需要保存 O(m * n) 个坐标。
#       原地修改 grid，不代表额外空间是 O(1)。
#
# 快速记忆思路
# 所有宝箱入队 → 取队头 → 检查四邻居 → 遇到 INF 就填距离并入队。
# 邻居距离 = 当前距离 + 1。
# 全部起点先入队，先进先出保最短；填写距离也标记访问。
#
# 口语讲述思路
#
# I'll use multi-source BFS, starting from all the treasure chests.
#
# First, I check if the grid is empty.
# Then I scan the grid and add every treasure chest to a queue.
# Each chest has a distance of zero.
#
# While the queue is not empty, I remove the cell at the front
# and check its four neighbors: up, down, left, and right.
#
# I skip a neighbor if it is out of bounds
# or its value is not INF.
# This skips water, treasure chests, and land that has already been visited.
#
# For an unvisited land cell, I set its distance
# to the current cell's distance plus one.
# Then I add it to the back of the queue.
#
# Updating the distance also marks the cell as visited,
# so I don't need a separate visited set.
#
# Since all chests start in the queue, BFS explores distance zero first,
# then distance one, then distance two, and so on.
# The first time I reach a land cell, I have found its shortest distance
# to any treasure chest, even if another chest is much farther away.
#
# Unreachable land stays INF.
# I modify the grid in place, so I don't return a new grid.
#
# The time complexity is O(m * n), where m and n are the grid dimensions.
# The space complexity is also O(m * n) in the worst case for the queue.