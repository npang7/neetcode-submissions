# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(
        self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # Both positions are empty.
        if p is None and q is None:
            return True

        # Only one position is empty.
        if p is None or q is None:
            return False

        # Both nodes exist, but their values differ.
        if p.val != q.val:
            return False

        # Compare the left subtrees.
        left_same = self.isSameTree(p.left, q.left)
        if not left_same:
            return False

        # Compare the right subtrees.
        right_same = self.isSameTree(p.right, q.right)
        return right_same

# I'll use recursive DFS to compare the two trees at corresponding positions.
#
# If both nodes are None, I return True.
# If only one is None, I return False because their structures differ.
# If both nodes exist but their values differ, I also return False.
#
# Otherwise, I recursively compare the left subtrees and the right subtrees.
# The trees are identical only if both comparisons return True.
# Using "and" lets me skip the right comparison if the left one returns False.
#
# The time complexity is O(n) in the worst case,
# because I compare every corresponding pair of nodes.
# The space complexity is O(h) for the recursion stack,
# where h is the tree's height.

# 思路：递归 DFS，同时比较两棵树对应位置的节点。
# 相同的条件：结构相同，并且对应节点的值相同。
#
# 1. 两个节点都为空：
#    - if p is None and q is None:
#          return True
#    - 这两个位置相同。
#
# 2. 只有一个节点为空：
#    - if p is None or q is None:
#          return False
#    - 两个都为空的情况已在上一步处理，所以这里表示只有一个为空。
#    - 说明结构不同。
#
# 3. 两个节点都存在，但值不同：
#    - if p.val != q.val:
#          return False
#
# 4. 当前两个节点匹配，继续比较左右子树：
#    - 左子树：self.isSameTree(p.left, q.left)
#    - 右子树：self.isSameTree(p.right, q.right)
#    - 两边都相同，当前整棵树才相同，因此用 and 连接。
#
# 5. 返回结果：
#    - return (
#          self.isSameTree(p.left, q.left)
#          and self.isSameTree(p.right, q.right)
#      )
#    - 左边返回 False 时，and 会短路，不再检查右边。
#    - 子调用的结果通过每层的 return 逐层返回。
#
# 注意：
# - 必须先检查 None，再访问 .val、.left 和 .right。
# - 不能只比较节点值，还必须比较它们所在的位置。
# - isSameTree 是类中的实例方法，递归调用需要写 self.isSameTree(...)。
#
# 时间复杂度：O(n)，最坏需要比较所有对应节点。
# 空间复杂度：O(h)，递归栈深度取决于树高，最坏为 O(n)。