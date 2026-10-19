from collections import defaultdict

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        # 用字典保存：台阶编号 → 到达该台阶的方法数
        dp = defaultdict(int)

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]