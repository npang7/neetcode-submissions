class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums == None:
            return 0
        maxsum = nums[0]
        currsum = 0
        for num in nums:
            if currsum < 0:
                currsum = 0
            currsum = currsum + num
            maxsum = max(maxsum,currsum)
        return maxsum