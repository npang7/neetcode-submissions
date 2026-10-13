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
                return 0

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