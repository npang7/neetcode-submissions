class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        res = []
        for i in range(len(nums)):
            want = target - nums[i]
            if nums[i] in seen :
                res = [seen.get(nums[i]) ,i]
            seen[want] = i
        return res