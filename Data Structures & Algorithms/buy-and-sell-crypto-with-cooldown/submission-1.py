class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # dp[i][0]：从第 i 天开始，手里没有币、可以买时的最大利润
        # dp[i][1]：从第 i 天开始，手里有币时的最大利润
        #
        # 多留两行，因为卖出后要读取 dp[i + 2][0]
        dp = [[0, 0] for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            # 没有币：今天跳过，或者今天买入
            dp[i][0] = max(
                dp[i + 1][0],
                -prices[i] + dp[i + 1][1]
            )

            # 有币：今天继续持有，或者今天卖出
            dp[i][1] = max(
                dp[i + 1][1],
                prices[i] + dp[i + 2][0]
            )

        return dp[0][0]