# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower, upper):
            if node is None:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            left_valid = dfs(node.left,lower,node.val)
            if left_valid != True:
                return False
            right_valid = dfs(node.right,node.val,upper)
            return right_valid

        return dfs(root,float("-inf"),float("inf"))