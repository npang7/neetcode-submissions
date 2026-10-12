class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        result = []
        path = []
        def backtrack():
            if len(path) == len(nums):
                result.append(path.copy())
                return
            
            for i in range(len(nums)):
                if used[i] == True:
                    continue
                
                path.append(nums[i])
                used[i] = True
                backtrack()

                path.pop()
                used[i] = False
         
        backtrack()
        return result