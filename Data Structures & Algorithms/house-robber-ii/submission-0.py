class Solution: # circle限定：第一间和最后一间，最多只能偷一间，也可以两间都不偷。
    def rob(self, nums: List[int]) -> int:
        # 只有一间房子时，直接拿走这间房子的钱
        if len(nums) == 1:
            return nums[0]

        # 计算一组直线排列的房子的最大金额
        def rob_linear(houses):
            m = len(houses)

            # dp[i]：考虑前 i 间房子，最多能偷到的钱
            dp = [0] * (m + 1)

            dp[0] = 0
            dp[1] = houses[0]

            for i in range(2, m + 1):
                # 不偷当前这间
                skip = dp[i - 1]

                # 偷当前这间
                take = dp[i - 2] + houses[i - 1]

                dp[i] = max(skip, take)

            return dp[m]

        # 情况一：排除最后一间 ， 这是截断list操作！
        without_last = rob_linear(nums[:-1])
        #表示从开头取到最后一个元素之前，也就是去掉最后一个元素。

        # 情况二：排除第一间
        without_first = rob_linear(nums[1:])
        #表示从下标 1 一直取到末尾，也就是去掉第一个元素。


        # 返回两种情况中的最大金额
        return max(without_last, without_first)

