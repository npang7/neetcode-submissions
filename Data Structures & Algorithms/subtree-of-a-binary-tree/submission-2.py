# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        if self.sameTree(root, subRoot):
            return True
        return (
            self.isSubtree(root.left, subRoot) 
            or self.isSubtree(root.right, subRoot))
    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if q is None or p is None:
            return False
        if q.val != p.val:
            return False
        return (self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right))