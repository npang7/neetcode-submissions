# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_so_far):
            if node is None:
                return 0

            # Check whether the current node is good.
            count = 0
            if node.val >= max_so_far:
                count = 1

            # Update the maximum before visiting the children.
            max_so_far = max(max_so_far, node.val)

            # Count good nodes in both subtrees.
            left_count = dfs(node.left, max_so_far)
            right_count = dfs(node.right, max_so_far)

            return count + left_count + right_count

        return dfs(root, root.val)
