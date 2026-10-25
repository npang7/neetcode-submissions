class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0
        farthest = nums[0]
        for i in range(len(nums)):
            if i > farthest:
                return False
            curr = nums[i] + i
            farthest = max(curr,farthest)
        return (farthest >= (len(nums)-1))