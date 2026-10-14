class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows = len(heights)
        cols = len(heights[0])
        
        pacific = set()
        atlantic = set()
        directions = [(-1, 0),(1, 0),(0, -1),(0, 1) ]

        # 反向搜索，记录能流到对应海洋的格子
        def dfs(r, c, reachable):
            # 当前格子已经搜索过，不重复处理
            if (r, c) in reachable:
                return

            reachable.add((r, c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # 邻居越界，跳过
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                # 反向搜索不能走向更低的位置
                if heights[nr][nc] < heights[r][c]:
                    continue

                dfs(nr, nc, reachable)

        # 左边接触太平洋，右边接触大西洋
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)

        # 上边接触太平洋，下边接触大西洋
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)

        result = []

        # 找出能流到两个海洋的格子
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result