# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def maxDepth(root):
            if root == None:
                return 0;
            #因为 maxDepth 定义在 diameterOfBinaryTree 内部，
            #它是局部函数, 不需要写self.maxDepth
            left_len = maxDepth(root.left)
            right_len = maxDepth(root.right)
            self.diameter = max(self.diameter, right_len+left_len)
            return 1 + max(right_len , left_len)
        maxDepth(root)
        return self.diameter