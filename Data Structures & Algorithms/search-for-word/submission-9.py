
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        directions = [(0,1),(0,-1),(-1,0),(1,0)]

        def backtrack(r,c,i):
            if r < 0 or r>=rows or c<0 or c>=cols:
                return False
            if (r,c) in visited or board[r][c] != word[i]:
                return False
            if len(word) -1 == i:
                return True
                
            #1. 选择当前格子
            visited.add((r,c))
            
            #2. 探索邻居
            for dr,dc in directions:
                if backtrack( r+dr, c+dc, i+1):
                    return True  #只要有一个方向成功,立刻返回True
                   
			# 3. 如果邻居探索失败，撤销选择
            visited.remove((r,c))
            return False

        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0):
                    return True
        return False
        
        
        