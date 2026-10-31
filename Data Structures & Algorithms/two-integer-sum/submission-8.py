class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        wait = {}
        res = []
        for i,num in enumerate(nums):
            want = target - num
            if num in wait :
                res = [wait.get(num) ,i]
            wait[want] = i
        return res