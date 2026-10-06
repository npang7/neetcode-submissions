# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0;
        def dfs(node, max_so_far):
            if node is None:
                return 0
            count = 0
            if node.val >= max_so_far:
                count += 1

            max_so_far = max(max_so_far , node.val)
            
            left_count = dfs(node.left,max_so_far)
            right_count = dfs(node.right,max_so_far)
            return left_count + right_count + count
        return dfs(root,root.val)