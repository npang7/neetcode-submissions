class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(0 , 9):
            count = {}
            for j in range(0 , 9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in count:
                    return False
                count[board[i][j]] = count.get(board[i][j] , 0) + 1
            
        for i in range(0 , 9):
            count = {}
            for j in range(0 , 9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in count:
                    return False
                count[board[j][i]] = count.get(board[j][i] , 0) + 1
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                count = {}
                for x in range(i , i+3):
                    for y in range(j,j+3):
                        if board[x][y] == ".":
                            continue
                        if board[x][y] in count:
                            return False 
                        count[board[x][y]] = count.get(board[x][y] , 0) + 1

        return True

