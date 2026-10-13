class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        minutes = 0
        fresh = 0
        queue = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c))
                elif grid[r][c]==1:
                    fresh += 1
                    
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue and fresh>0: # and fresh>0要记得！！
        # 加入 fresh > 0 后，所有新鲜水果腐烂时就停止，不会多处理最后一层。

            level_size = len(queue)
            #r,c = queue.popleft() 不是在这里！！
            for _ in range(level_size):
                r,c = queue.popleft() 
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc   
                    if (nr<0 or nc<0 or nr>=rows or nc>=cols) :
                        continue
                    if grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr,nc)) #不要忘记！！
            minutes +=1 
            
        if fresh>0:
            return -1
        return minutes    