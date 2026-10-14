class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows = len(heights)
        cols = len(heights[0])
        atlantic = set()
        pacific = set()
        directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]
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
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)

        for c in range(cols):
            dfs(0,c,pacific)
            dfs( rows -1, c , atlantic)
        
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
        return result
