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


# Rotate Image（旋转图像）
#
# 一、分类 / 关键词
# - Array / List（数组 / 列表）：二维列表存储矩阵。
# - Matrix（矩阵）：通过行列下标访问、交换元素。
# - Math（数学）：利用转置和翻转实现旋转。
# - In-place（原地操作）：直接修改输入，不创建另一个矩阵。
#
# 二、记忆思路：先转置，再反转每一行
#
# 1. 转置：交换行下标和列下标。
#    - 交换 matrix[row][col] 与 matrix[col][row]。
#    - 主对角线上的元素不动。
#    - 只处理主对角线上方，即 col > row 的位置。
#    - row 遍历 range(n)，col 遍历 range(row + 1, n)。
#    - 每对元素只交换一次，避免交换回来。
#
# 2. 每一行左右反转。
#    - 遍历每个行列表，调用 row.reverse()。
#    - 原来的第一列变成最后一列，第二列变成倒数第二列。
#
# 3. 两步组合就是顺时针旋转 90°。
#    - 转置：(row, col) → (col, row)。
#    - 左右反转：(col, row) → (col, n - 1 - row)。
#
# 快速记忆：行列交换，再左右翻转。
#
# 三、易错点
# - 转置不能遍历所有位置都交换，否则每对元素交换两次，会恢复原样。
# - 反转的是“每一行”，不是整个矩阵的行顺序。
#   row.reverse()：这一行左右翻转。
#   matrix.reverse()：所有行上下翻转，含义不同。
# - 顺序不能随便交换：
#   转置 → 每行反转：顺时针 90°。
#   每行反转 → 转置：逆时针 90°。
# - 不能直接把每个元素赋到旋转后的坐标，会覆盖尚未移动的数据。
# - 题目要求修改原矩阵，不需要返回新矩阵。
#
# 四、相关 Python 基础
# - n = len(matrix)：方阵的行数与列数相同。
# - matrix[row][col]：先行、后列。
# - range(row + 1, n)：从对角线右侧开始，不包含 n。
#
# - 使用临时变量交换：
#   temp = a
#   a = b
#   b = temp
# - 也可以使用 Python 同时赋值：a, b = b, a。
#
# - for row in matrix： !!!!
#   row 是原矩阵中的行列表，不是行下标，也不是副本。
#   调用 row.reverse() 会直接修改原矩阵中的这一行。
#
# - reverse() 原地修改列表，返回 None。
#   不要写 row = row.reverse()。
# - row[::-1] 会创建一个新的反转列表。
#   仅写 row = row[::-1] 不会替换 matrix 中原来的行。
#
# 五、复杂度
# - 时间：O(n²)，转置和逐行反转都需要 O(n²)。
# - 额外空间：O(1)，只使用临时变量，reverse() 也是原地操作。
