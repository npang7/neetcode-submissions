class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        tuple_nums = tuple(nums)
        for num in nums:
            product = 1
            origin_nums = list(tuple_nums)
            origin_nums.remove(num)
            for n in origin_nums:
                product = product * n
            res.append(product)
        return res