class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            coin = coins[i-1]
            for a in range(amount+1):
                dp[i][a] = dp[i-1][a]
                if a >= coin:
                    dp[i][a] += dp[i][a-coin]
        return dp[n][amount]