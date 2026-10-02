# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def depth(node):
            if node is None:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # 更新经过当前节点的最长路径
            self.diameter = max(
                self.diameter,
                left_depth + right_depth
            )

            # 返回以当前节点为根的子树深度
            return 1 + max(left_depth, right_depth)

        depth(root)
        return self.diameter