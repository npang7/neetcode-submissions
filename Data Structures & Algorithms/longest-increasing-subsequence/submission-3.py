class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i]：必须以 nums[i] 结束的最长递增子序列长度
        # 单独选择当前元素，长度至少为 1
        dp = [1] * n

        for i in range(1, n):
            # 检查当前元素之前的每一个位置
            for j in range(i):

                # 当前元素可以接在 nums[j] 后面
                if nums[j] < nums[i]:
                    candidate = dp[j] + 1

                    # 保留以当前元素结束的最长长度
                    dp[i] = max(dp[i], candidate)

        # 最长递增子序列可以结束在任意位置
        return max(dp)