class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for current_amount in range(1, amount+1):
            for coin in coins:
                if coin > amount:
                    continue
                remaining = current_amount - coin
                candidate = dp[remaining] + 1 #每个不同数值的coin有不同的candidate
                dp[current_amount] = min(dp[current_amount] ,candidate)
        if (dp[amount] == float("inf")):
            return -1
        return dp[amount]