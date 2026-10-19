class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if (total % 2 != 0) :
            return False
        target = total // 2
        dp = [False] * (target+1)
        dp[0] = True
        for num in nums:
            for current_sum in range(target, num-1, -1):
                remaining = current_sum - num
                if dp[remaining]:
                    dp[current_sum] = True
        return dp[target]