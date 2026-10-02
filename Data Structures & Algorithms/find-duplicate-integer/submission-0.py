class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        # Find a meeting point inside the cycle.
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        # 第一阶段结束时，指针已经在相遇位置，
        # 也就是已经处于“从入口走了 x 步”的位置


        # To find the entrance of the cycle.
        slow2 = 0

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow


# 再解释一下，为什么第二阶段一定能找到入口。
# 设：
# - L：从下标 0 到环入口的步数。
# - x：从环入口到第一阶段相遇位置的距离。
# - C：环的长度。
# 第一阶段相遇时，快指针走过的路程是慢指针的两倍。它比慢指针多走的路程，必须是环长度的整数倍。因此可以得到：  L + x 是 C 的整数倍！
# 所以，从相遇位置再走 L 步，就会回到环入口：在环内走过的距离相当于 x + L，恰好是若干个完整的圈。
# 与此同时，从下标 0 出发的另一个指针走 L 步，也正好到入口。因此它们会在那里相遇。
# 在刚才的例子中：
# L = 3  # 从 0 经过 1、3，走到入口 2x = 1  # 从入口 2 走到相遇位置 4C = 2  # 环包含 2、4


# L + x = 4，是环长度 2 的整数倍，所以两个指针一起走三步，都会到达入口 2。
# - 时间复杂度：O(n)。
# - 额外空间复杂度：O(1)，只使用几个下标变量。