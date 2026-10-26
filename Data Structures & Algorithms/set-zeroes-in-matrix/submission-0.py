class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_rows = set()  # 需要清零的行号
        zero_cols = set()  # 需要清零的列号
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for i in range(rows):
            for j in range(cols):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0
        
        





#你一会讲一下以后在做题的时候如何决定使用什么样的数据结构