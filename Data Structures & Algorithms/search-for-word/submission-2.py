class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def backtrack(r,c,i):
            if r < 0 or r>=rows or c<0 or c>=cols:
                return False
            if (r,c) in visited or board[r][c] != word[i]:
                return False
            if len(word) -1 == i:
                return True
            
            visited.add((r,c))
            
            found = (backtrack(r-1,c,i+1) or
            backtrack(r+1,c,i+1) or backtrack(r,c-1,i+1)
            or backtrack(r,c+1,i+1)
            )
            if found == True:
                return  True

            visited.remove((r,c))
            return False


        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0):
                    return True
        return False