class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = [0] * (max(nums)-min(nums)+1)

        for num in nums:
            count[num - min(nums)] = 1   #考虑到存在负数，整体右移

        length = 0
        max_length = 0

        for i in range(0 , len(count)):
            if count[i] == 0:
                if length > max_length:
                    max_length = length
                length = 0
            if count[i] != 0:
                length += 1
                if length > max_length:
                    max_length = length

        return max_length
