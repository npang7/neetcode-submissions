# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        count = 0

        while current is not None or stack:
            # 一直向左走，把沿途的节点保存到栈中
            while current is not None:
                stack.append(current)
                current = current.left

            # 左边已经走完，访问当前应该处理的节点
            current = stack.pop()
            count += 1

            # 中序遍历中的第 k 个节点，就是第 k 小的节点
            if count == k:
                return current.val

            # 当前节点访问完毕，接着处理它的右子树
            current = current.right