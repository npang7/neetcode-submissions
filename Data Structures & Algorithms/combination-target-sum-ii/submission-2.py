class Solution:
    def combinationSum2(
        self, candidates: List[int], target: int) -> List[List[int]]:
        # 排序，让相同的数字相邻
        candidates.sort()

        result = []
        path = []

        def backtrack(i, total):
            #1. 找到符合要求的组合
            if total == target:
                result.append(path.copy())
                return

            #2. 没有候选元素，或者总和已经超过目标
            if i == len(candidates) or total > target:
                return

            #3. 第一种选择：选当前元素
            path.append(candidates[i])
            # 当前元素只能使用一次，所以考虑下一个位置
            backtrack(i + 1, total + candidates[i])

            #4.第二种选择：不选当前元素，撤销这一层的选择
            path.pop()
            # 跳过后面所有相同值的元素，避免重复组合
            next_i = i + 1
            #增加的部分-------------------
            #不选当前元素还要跳过后面所有相同值的元素，避免重复组合
            while (
                next_i < len(candidates)
                and candidates[next_i] == candidates[i]
            ):
                next_i += 1
            #----------------------------
            # 从下一个不同的数字继续探索
            backtrack(next_i, total)

        backtrack(0, 0)
        return result
