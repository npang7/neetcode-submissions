# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 空树可以看作任何树的子树
        if subRoot is None:
            return True
        # 大树为空，但 subRoot 不为空：无法找到
        if root is None:
            return False

        # 检查当前节点是否是匹配的起点
        if self.sameTree(root, subRoot):
            return True

        # 否则，继续去左右子树中寻找
        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )


    def sameTree(
        self, p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return (
            self.sameTree(p.left, q.left)
            and self.sameTree(p.right, q.right)
        )