class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        res = 0
        count = {0:1}
        for num in nums:
            prefix_sum = prefix_sum + num

            need_sum = prefix_sum - k
            res += count.get(need_sum, 0)

            count[prefix_sum] = count.get(prefix_sum, 0) + 1

        return res