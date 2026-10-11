class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        total = 0
        result = []
        path = []
        def backtrack(i, total):
            if total == target:
                result.append(path.copy())
                return
            if i == len(nums) or total > target:
                return

            path.append(nums[i])
            backtrack(i , total+nums[i])

            path.pop()
            backtrack(i+1,total)
        
        backtrack(0,0)
        return result

        