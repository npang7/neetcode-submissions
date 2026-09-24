class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_num = max(nums)
        min_num = min(nums)
        count = [0] * (max_num-min_num+1)

        for num in nums:
            count[num - min_num] = 1   #考虑到存在负数，整体右移

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
                    max_length = length   #不要忘了这里也要更新max！，如果最后一个结尾是1，如果不更新max会直接漏掉！

        return max_length
