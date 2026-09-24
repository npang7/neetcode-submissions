class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        tuple_nums = tuple(nums)
        for num in nums:
            product = 1
            fix_nums = list(tuple_nums)
            new_nums = fix_nums
            new_nums.remove(num)
            for n in new_nums:
                product = product * n
            res.append(product)
        return res