class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax = 1
        curMin = 1
        for num in nums:
            prev_max = curMax
            curMax = max(num , num*curMax, num*curMin)
            curMin = min(num, num*curMin, num*prev_max)
            res = max(res, curMax)
        return res