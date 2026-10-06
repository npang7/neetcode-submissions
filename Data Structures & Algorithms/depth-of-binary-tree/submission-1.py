# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)

# I’ll use recursion to find the maximum depth.
# If the current node is null, I return zero.
# Otherwise, I recursively calculate the maximum depth of the left and right subtrees.
# Then I return the larger of the two depths plus one, to include the current node.
# The time complexity is O(n), because I visit every node once. The space complexity is O(h), where h is the height of the tree, due to the recursion stack.
#注意深度不是几条边，是指几个变深的node！！