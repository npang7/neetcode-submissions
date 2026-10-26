class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        bottom = rows -1
        left = 0
        right = cols - 1

        res = []
        while top <= bottom and left <= right :
            for col in range(left, right+1): #向右, 行固定为 top
                res.append(matrix[top][col])
            top += 1
            for row in range(top ,bottom+1):#向下, 列固定为 right
                res.append(matrix[row][right]) 
            right -= 1
            if top > bottom or left > right: #在向左之前补检查！！重要
                break
            for col in range(right,left-1,-1): #向左, 行固定为 bottom
                res.append(matrix[bottom][col])
            bottom -=1
            for row in range(bottom,top-1, -1): #向上, 列固定为 left
                res.append(matrix[row][left])
            left +=1

        return res

    
# 记住：进入一圈时有剩余区域，不代表走到这一圈中途时还有

# Spiral Matrix（螺旋矩阵）
#
# 一、分类 / 关键词
# - Array / List（数组 / 列表）：二维列表存储矩阵。
# - Matrix（矩阵）：通过行列下标访问元素。
# - Simulation（模拟）：按右、下、左、上的顺序遍历。
# - Boundary Tracking（边界维护）：逐步缩小未遍历区域。
#
# 二、记忆思路
# 1. 初始化四个边界，均表示包含在内的下标：
#    - top = 0，bottom = 行数 - 1。
#    - left = 0，right = 列数 - 1。
#
# 2. 用 while 重复处理当前区域的外圈。
#    - 条件：top <= bottom and left <= right。
#    - 只剩一行或一列时，也仍然需要处理，所以使用 <=。
#
# 3. 按四个方向遍历，每处理完一条边，就缩小对应边界：
#    - 向右：行固定为 top，列从 left 到 right；之后 top += 1。
#    - 向下：列固定为 right，行从 top 到 bottom；之后 right -= 1。
#    - 检查是否还有剩余区域，没有就 break。！！！！！！！！！
#    - 向左：行固定为 bottom，列从 right 到 left；之后 bottom -= 1。
#    - 向上：列固定为 left，行从 bottom 到 top；之后 left += 1。
#
# 4. 循环结束，返回结果列表。
#
# 快速记忆：
# 右、下、检查、左、上；
# 走完哪条边，就收缩哪条边。
#
# 三、易错点
# - 边界变量与遍历变量分开：
#   top、bottom、left、right 记录边界；row、col 负责移动。
# - 不要写 for top in ...，否则会覆盖上边界。
# - 固定下标明确使用对应边界，不依赖上一个循环留下的 row / col。
# - 左边界向右收缩是 left += 1，不是 left -= 1。
# - 每条边处理完立即更新边界，避免重复访问角落。
#
# - 向右、向下之后，必须检查：
#   if top > bottom or left > right:
#       break
# - 只剩一行时，向右可能已取完，继续向左会重复。
# - 只剩一列时，向下可能已取完，继续向上会重复。
# - 外层 while 只在每轮开始时检查条件，中途边界失效不会自动停止。
#
# 四、Python 基础
# - len(matrix)：行数。
# - len(matrix[0])：列数。
# - matrix[row][col]：先行、后列。
# - for 会自动给循环变量赋值，不需要提前初始化 row、col。！！！！
#
# - range 不包含结束值：
#   range(left, right + 1)：从 left 到 right，包含两端。
#   range(top, bottom + 1)：从 top 到 bottom，包含两端。
#   range(right, left - 1, -1)：从 right 倒序到 left。
#   range(bottom, top - 1, -1)：从 bottom 倒序到 top。
# - range(2, 2) 为空，循环不执行。
#
# - break：结束最近一层循环；这里在 while 中、各个 for 之外使用，
#   所以结束 while，随后执行循环外的返回语句。
# - and：行、列两个范围都有效，才继续。
# - or：行、列任意一个范围失效，就停止。
#
# 五、复杂度
# - 时间：O(m × n)，每个元素访问一次。
# - 额外空间：O(1)，不计返回结果，只维护固定数量的变量。
# - 返回结果需要 O(m × n) 空间。
