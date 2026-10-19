class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) #楼顶的下标index

        # dp[i]：到达位置 i 时，已经支付的最小总费用
        # 楼顶的位置是 n，所以需要下标 0 到 n
        dp = [0] * (n + 1)

        # 可以直接从位置 0 或位置 1 开始
        dp[0] = 0
        dp[1] = 0

        # 从位置 2 开始，计算到楼顶 n
        for i in range(2, n + 1):
            # 从前一个位置爬 1 级过来
            one_step = dp[i - 1] + cost[i - 1]

            # 从前两个位置爬 2 级过来
            two_steps = dp[i - 2] + cost[i - 2]

            # 选择花费较少的方式
            dp[i] = min(one_step, two_steps)
            # dp[i]：到达位置 i 时，已经支付的最小总费用
            
        return dp[n]