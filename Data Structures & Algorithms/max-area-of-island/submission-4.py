class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        # 返回从当前位置开始，新访问到的陆地数量
        def dfs(r, c):
            # 越界、是水或者已经访问过，都不贡献面积
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0):
                return 0  #注意是return 0 而不是只有return！！

            # 标记当前陆地，避免重复计算
            grid[r][c] = 0

            # 计算四个方向新访问到的陆地数量
            up_area = dfs(r - 1, c)
            down_area = dfs(r + 1, c)
            left_area = dfs(r, c - 1)
            right_area = dfs(r, c + 1)

            # 当前陆地算 1，再加上四个方向的结果
            return 1 + up_area + down_area + left_area + right_area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # 从未访问的陆地出发，计算整座岛的面积
                    area = dfs(r, c)
                    # 更新目前找到的最大面积
                    max_area = max(max_area, area)

        return max_area

# 中文思路清单（DFS：计算每座岛的面积，保留最大值）
#
# 1. 初始化关键变量。
#    - rows = len(grid)：网格的行数。
#    - cols = len(grid[0])：网格的列数。
#    - max_area = 0：目前找到的最大岛屿面积。
#    - r 表示行号，c 表示列号。
#    - 题目保证网格非空，所以可以直接读取 grid[0]。
#
# 2. 用两个 for 循环逐个检查格子。
#    - 外层遍历行，内层遍历列。
#    - 如果 grid[r][c] == 1，说明遇到了尚未访问的陆地。
#    - 调用 area = dfs(r, c)，计算这座岛的面积。
#
# 3. 每次进入 DFS，先检查结束条件。
#    - r < 0 或 r >= rows：行号越界，返回 0。
#    - c < 0 或 c >= cols：列号越界，返回 0。
#    - grid[r][c] == 0：是水或者已经访问过，返回 0。
#    - 必须先判断越界，再读取 grid[r][c]。
#    - 返回 0 表示当前位置没有新增陆地，不贡献面积。
#
# 4. 如果当前位置是未访问的陆地，先标记它。
#    - 执行 grid[r][c] = 0，表示当前陆地已经访问过。
#    - 必须先标记，再探索邻居，避免在相邻格子之间来回递归。
#    - 这种写法会修改原始 grid，不需要额外的 visited 集合。
#
# 5. 递归探索上下左右，得到各方向新访问的陆地数量。
#    - up_area = dfs(r - 1, c)：上方的搜索结果。
#    - down_area = dfs(r + 1, c)：下方的搜索结果。
#    - left_area = dfs(r, c - 1)：左方的搜索结果。
#    - right_area = dfs(r, c + 1)：右方的搜索结果。
#    - 不搜索对角线，因为斜着相连的陆地不属于同一座岛。
#    - 前面的搜索标记过的陆地，后面的搜索会跳过，不会重复计算。
#
# 6. 返回当前这次 DFS 找到的陆地总数。
#    - 返回 1 + up_area + down_area + left_area + right_area。
#    - 其中的 1 表示当前这一块陆地。
#    - 每次递归把结果返回给调用它的那一层。
#    - 最外层的 dfs(r, c) 最终返回整座岛的面积。
#
# 7. DFS 完成后，更新最大面积并继续扫描。
#    - area：刚刚搜索完的这座岛的面积。
#    - max_area = max(max_area, area)：保留较大的面积。
#    - 这座岛的陆地已经全部变成 0，之后不会重新计算。
#    - 遇到下一块 1 时，再计算下一座岛的面积。
#
# 8. 所有格子检查完成后，返回 max_area。
#    - 如果没有陆地，max_area 始终是 0。
#    - 否则，max_area 就是所有岛屿面积中的最大值。
#
# 9. 容易混淆的地方。
#    - 行号 r 与 rows 比较，列号 c 与 cols 比较。
#    - 这道题使用整数 1 和 0，不是字符串 "1" 和 "0"。
#    - DFS 的结束条件必须 return 0，不能只写 return。
#      只写 return 会返回 None，后面与整数相加时会报错。
#    - 当前陆地的 1 和四个方向的结果相加，不能只取最大方向。
#      我们需要计算整座岛的所有陆地，而不是最长的一条路径。
#    - 不需要把访问过的格子恢复成 1，否则可能重复计算。
#    - Number of Islands 数岛屿数量，这道题计算每座岛的面积。
#
# 10. 时间和空间复杂度。
#     - 假设网格有 m 行、n 列。
#     - 时间复杂度：O(m * n)。
#       外层循环检查所有格子，每块陆地最多被标记一次，
#       每次只探索四个方向。
#     - 空间复杂度：O(m * n)。
#       最坏情况下，递归调用栈的深度可能达到 m * n。
#       没有 visited 集合，不代表空间复杂度是 O(1)。
#
# 快速记忆思路
# 扫描格子 → 遇到 1 → DFS 计算整座岛的面积 → 更新最大值。
# DFS：无效位置返回 0；有效陆地先标记，再返回 1 + 四个方向的结果。
#
# 口语讲述思路
#
# If I can modify the input grid, I'll use depth-first search.
# I mark visited land by changing it from one to zero.
#
# First, I store the number of rows and columns
# and initialize the maximum area to zero.
#
# Then I scan every cell in the grid.
# Whenever I find a one, I start DFS to calculate that island's area.
#
# In DFS, I return zero if the position is out of bounds
# or the cell is zero, since it doesn't add any new land.
#
# Otherwise, I mark the current cell as visited
# before exploring its four neighbors.
# I return one for the current cell, plus the results
# from the up, down, left, and right neighbors.
#
# After DFS finishes, I compare the island's area with the current maximum
# and keep the larger value.
# Since the island has been marked, I won't count its land again.
#
# Finally, I return the maximum area.
# If there is no land, the result stays zero.
#
# The time complexity is O(m * n), where m and n are the grid dimensions.
# The space complexity is also O(m * n) in the worst case
# because of the recursion stack.