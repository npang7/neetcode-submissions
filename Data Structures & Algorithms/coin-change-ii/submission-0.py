class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        # dp[i][a]：用前 i 种硬币凑出金额 a 的组合数
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # 不用任何硬币凑出 0 元：空组合，共 1 种
        dp[0][0] = 1

        for i in range(1, n + 1):
            coin = coins[i - 1]

            for a in range(amount + 1):
                # 不使用当前面额
                dp[i][a] = dp[i - 1][a]

                # 至少使用一枚当前面额
                if a >= coin:
                    dp[i][a] += dp[i][a - coin]

        return dp[n][amount]