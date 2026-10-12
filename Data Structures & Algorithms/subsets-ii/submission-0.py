class Solution: #沿用 Combination Sum II 的去重方法
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 排序，让相同的数字相邻
        nums.sort()
        result = []
        path = []

        def backtrack(i):
            # 所有元素都考虑完，保存当前子集
            if i == len(nums):
                result.append(path.copy())
                return

            # 第一种选择：选当前元素
            path.append(nums[i])
            # 每个位置只能使用一次，继续考虑下一个位置
            backtrack(i + 1)

            # 第二种选择：不选当前元素，
            # 后面的和这个元素相同的也不要，避免重复
            # 撤销这一层的选择
            path.pop()
            # 跳过后面所有相同的数字，避免重复子集
            #--------------------
            next_i = i + 1
            while next_i < len(nums) and nums[next_i] == nums[i]:
                next_i += 1
            #--------------------
            backtrack(next_i)

        backtrack(0)
        return result