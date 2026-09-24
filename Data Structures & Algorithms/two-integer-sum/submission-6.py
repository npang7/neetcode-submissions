class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,num in enumerate(nums):
            map[num] = i
        for i,num in enumerate(nums):
            diff = target - num
            if diff in map and map[diff]!=i:
                return [i,map[diff]]
        return []