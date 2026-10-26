class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for row in range(n):
            for col in range(row + 1, n):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp       
        for row in matrix:
            row.reverse()
        



# 顺时针旋转 90° 的直接坐标规律是：
# # 原坐标 → 旋转后的坐标
# (row, col) → (col, n - 1 - row)


# 第一种方法先tranpose再reverse其实就是把直接坐标公式拆成两步：
# 第一步：转置(row, col) → (col, row)
# 第二步：每行左右反转(col, row) → (col, n - 1 - row)
