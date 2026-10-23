class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(1,n+1):
            num = nums[i-1]
            for total,sign_count in dp[i-1].items():
                dp[i][total+num] += sign_count
                dp[i][total-num] += sign_count

        return dp[n][target]