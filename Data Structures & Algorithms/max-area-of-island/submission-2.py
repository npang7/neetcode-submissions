class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        def dfs(r,c):
            if (r<0 or c<0 or r>=rows or c >=cols 
                or grid[r][c]==0):
                return 0  #注意是return 0 而不是只有return！！
                
            grid[r][c] = 0

            up_area = dfs(r-1,c)
            down_area = dfs(r+1,c)
            left_area = dfs(r,c-1)
            right_area = dfs(r, c+1)
            return 1+ up_area + down_area + left_area + right_area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    max_area = max(max_area, area)
        return max_area