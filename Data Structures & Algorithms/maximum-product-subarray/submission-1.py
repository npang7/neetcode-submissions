class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        # max_dp[i]：以 nums[i] 结束的子数组的最大乘积
        # min_dp[i]：以 nums[i] 结束的子数组的最小乘积
        max_dp = [0] * n
        min_dp = [0] * n

        # 以第一个元素结束，只能选择它自己
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]

        for i in range(1, n):
            current = nums[i]

            # 尝试从当前元素开始，或者接在前面的子数组后面
            max_dp[i] = max(
                current,
                max_dp[i - 1] * current,
                min_dp[i - 1] * current
            )

            min_dp[i] = min(
                current,
                max_dp[i - 1] * current,
                min_dp[i - 1] * current
            )

        # 最大乘积可能结束在任意位置
        return max(max_dp)