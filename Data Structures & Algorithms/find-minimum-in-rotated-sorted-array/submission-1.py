class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
        
# I use binary search to find the minimum. I keep two pointers, left and right, and compare the middle element with the rightmost element in the current search range.
# If nums[mid] is greater than nums[right], the minimum must be to the right of mid, so I set left to mid + 1.
# Otherwise, the minimum is at mid or to its left, so I set right to mid. I keep mid because it could be the minimum.
# When left and right meet, I return the element at that index. Each step cuts the search range roughly in half, so the time complexity is O(log n) and the extra space is O(1).