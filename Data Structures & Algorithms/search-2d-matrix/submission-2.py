class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols -1
        while left <= right:
            mid = (left + right)//2
            row_index = mid//cols #前面已经经过了多少个完整的行，也就是行号
            col_index = mid % cols # 在当前行走到了第几个位置，也就是列号
            value = matrix[row_index][col_index]
            if value == target:
                return True
            elif target < value:
                right = mid -1
            else:
                left = mid +1
        return False
            