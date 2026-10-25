class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = nums[0]
        step = 0
        end = 0
        curr = 0
        for i in range(len(nums) - 1): #只检查到倒数第二个下标
            curr =  i + nums[i]
            farthest = max(curr,farthest)
            if i == end:
                end = farthest
                step += 1
        return step

            