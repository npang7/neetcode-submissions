class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_length = 0
        length = 1
        for num in set_nums:
            if num - 1 not in set_nums:
                length = 1
                while num + length in set_nums:
                    length +=1
            max_length = max(max_length, length)

        return max_length
