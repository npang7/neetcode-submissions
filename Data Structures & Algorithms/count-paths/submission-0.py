class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[r][c] 表示到达第 r 行、第 c 列格子的走法数
        dp = [[1] * n for _ in range(m)] #记住写法

        # 第一行和第一列已经初始化为 1
        # 从第二行、第二列开始计算
        for r in range(1, m):
            for c in range(1, n):
                # 到达当前格子，可以从上方或左边过来
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        # 右下角的值就是总走法数
        return dp[m - 1][n - 1]