class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        def backtrack(i):
            if i == len(nums):
                result.append(path.copy())
                return
            
            path.append(nums[i])
            backtrack(i+1)

            path.pop() #不是！！path.pop(nums[i])，pop会自动选择
            backtrack(i+1)

        backtrack(0)
        return result