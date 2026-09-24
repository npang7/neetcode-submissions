class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            # 跳过重复的第一个数字
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]

                if current_sum < 0:
                    j += 1

                elif current_sum > 0:
                    k -= 1

                else:
                    res.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # 跳过重复的 j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # 跳过重复的 k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return res