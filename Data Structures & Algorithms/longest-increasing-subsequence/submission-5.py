class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n #dn[i]：以nums[i]结尾的subsequence最大长度
        for i in range(1,n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    candidate = dp[j] + 1
                    dp[i] = max(dp[i], candidate)
        return max(dp)
        