class Solution:
    def climbStairs(self, n: int) -> int:
        # 只有 1 级时有 1 种走法，2 级时有 2 种走法
        if n <= 2:
            return n

        # dp[i]：从地面到达第 i 级台阶的方法总数
        # 创建 n + 1 个位置，让下标可以直接使用 1 到 n
        dp = [0] * (n + 1)

        # 初始值
        dp[1] = 1
        dp[2] = 2

        # 从第 3 级开始，一直计算到第 n 级
        for i in range(3, n + 1):
            # 最后爬 1 级，或最后爬 2 级
            dp[i] = dp[i - 1] + dp[i - 2]

        # 返回到达第 n 级的方法总数
        return dp[n]