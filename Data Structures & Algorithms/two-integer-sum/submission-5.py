class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in prevmap:
                return [prevmap[diff], i]
            else: prevmap[num] = i
        return []