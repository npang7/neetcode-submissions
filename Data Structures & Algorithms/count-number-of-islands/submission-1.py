class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        # 记录已经访问过的陆地坐标
        visited = set()
        islands = 0

        # 从 (r, c) 开始，访问与它连通的所有陆地
        def dfs(r, c):
            # 超出网格范围，停止探索
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            # 当前格子是水，或者已经访问过，停止探索
            if grid[r][c] == "0" or (r, c) in visited:
                return

            # 先标记当前陆地，避免后续又走回来
            visited.add((r, c))

            # 探索上下左右四个方向
            dfs(r - 1, c)  # 上
            dfs(r + 1, c)  # 下
            dfs(r, c - 1)  # 左
            dfs(r, c + 1)  # 右

        # 逐个检查网格中的格子
        for r in range(rows):
            for c in range(cols):
                # 找到没有访问过的陆地，说明发现了一座新岛
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1

                    # 把这座岛上的所有陆地都标记为已访问
                    dfs(r, c)

        return islands
# 中文思路清单（DFS：把访问过的陆地改成 "0"）
#
# 1. 检查网格是否为空。
#    - 如果 grid 为空，或者第一行没有格子，直接返回 0。
#
# 2. 初始化关键变量。
#    - islands = 0：记录已经发现的岛屿数量。
#    - rows = len(grid)：网格的行数。
#    - cols = len(grid[0])：网格的列数。
#    - r 表示行号，c 表示列号，下标都从 0 开始。
#
# 3. 用两个 for 循环逐个检查格子。
#    - 外层遍历行，内层遍历列。
#    - 按照从左到右、从上到下的顺序检查整个网格。
#
# 4. 如果当前格子是 "1"，说明发现了一座新岛屿。
#    - 原来的水是 "0"，访问过的陆地也会被改成 "0"。
#    - 因此，仍然是 "1" 的格子一定是尚未访问的陆地。
#    - 执行 islands += 1。
#    - 调用 dfs(r, c)，访问这座岛上的所有陆地。
#
# 5. 每次进入 dfs，先检查是否需要结束当前调用。
#    - r < 0 或 r >= rows：行号越界，返回。
#    - c < 0 或 c >= cols：列号越界，返回。
#    - grid[r][c] == "0"：是水或者已访问的陆地，返回。
#    - 必须先检查越界，再读取 grid[r][c]。
#    - 注意：r 与 rows 比较，c 与 cols 比较。
#
# 6. 如果当前位置是未访问的陆地，标记并探索邻居。
#    - 先执行 grid[r][c] = "0"，标记为已访问。
#    - 必须先标记，再递归，避免相邻格子之间来回搜索。
#    - dfs(r - 1, c)：探索上方。
#    - dfs(r + 1, c)：探索下方。
#    - dfs(r, c - 1)：探索左侧。
#    - dfs(r, c + 1)：探索右侧。
#    - 只探索上下左右，不探索对角线。
#
# 7. 当前岛屿搜索完成后，继续外层循环。
#    - dfs(r, c) 完整结束后，for 循环才检查下一个格子。
#    - 同一座岛的所有陆地已经变成 "0"，不会再次计数。
#    - 遇到下一块 "1" 时，再增加 islands 并搜索新岛屿。
#    - 所有格子检查完成后，返回 islands。
#
# 8. 容易混淆的地方。
#    - islands += 1 在外层循环中执行，DFS 内部不增加计数。
#    - 一座岛可以有很多块陆地，但只增加一次计数。
#    - DFS 中的 return 只结束当前调用，调用它的函数会继续执行。
#    - 不需要把 "0" 恢复成 "1"，因为要一直保留已访问的标记。
#    - 这种写法会修改原始 grid，所以不需要额外的 visited 集合。
#    - 格子里的值是字符串，应该比较 "1" 和 "0"，不是整数 1 和 0。
#
# 9. 时间和空间复杂度。
#    - 假设网格有 m 行、n 列。
#    - 时间复杂度：O(m * n)。
#      每块陆地最多被标记一次，每次只探索四个方向。
#      外层循环也只检查全部 m * n 个格子一次。
#    - 空间复杂度：O(m * n)。
#      最坏情况下，递归调用栈的深度可能达到 m * n。
#      虽然没有 visited 集合，但递归栈仍然占用空间。
#
# 快速记忆思路
# 扫描格子 → 遇到 "1" 就计数 → DFS 把整座岛变成 "0" → 继续扫描。
# 外层循环数岛屿，DFS 标记整座岛。
#
# 口语讲述思路
#
# Assuming I can modify the input grid, I'll use depth-first search.
#
# First, I check if the grid is empty. If it is, I return zero.
# Then I store the number of rows and columns and initialize the island count.
#
# I scan the grid one cell at a time.
# Whenever I find a cell with "1", I count it as a new island
# and start DFS from that cell.
#
# In DFS, I return if the position is out of bounds or the cell is "0".
# Otherwise, I change the cell to "0" to mark it as visited.
# Then I explore its four neighbors: up, down, left, and right.
#
# I mark the cell before visiting its neighbors so I don't keep
# moving back and forth between the same cells.
#
# Once DFS finishes, all the land in that island has been marked.
# The outer loops then continue scanning, so I won't count that island again.
#
# Finally, I return the island count.
#
# The time complexity is O(m * n), where m and n are the grid dimensions.
# The space complexity is also O(m * n) in the worst case
# because of the recursion stack.
        