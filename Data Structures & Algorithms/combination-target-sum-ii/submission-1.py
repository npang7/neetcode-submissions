class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() 
        #返回的是None，不要写candidates=candidates.sort() ！！是错误的

        path = []
        result = []

        def backtrack(i, total):
            if total == target:
                result.append(path.copy())
                return
            if i == len(candidates) or total > target:
                return
            #1.
            path.append(candidates[i])
            backtrack(i+1,total+candidates[i])
            #2.
            path.pop()
            next_i = i + 1
            while next_i < len(candidates) and candidates[next_i] == candidates[i]:
                next_i += 1
            backtrack(next_i, total)
                
        backtrack(0,0)
        return result