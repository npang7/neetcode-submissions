# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = collections.deque()
        result = []
        queue.append(root)
        while queue: # ！= is not None，因为空队列也不是none，会一直在循环里
            level_len = len(queue)
            level = []
            for i in range(level_len):
                root = queue.popleft()
                level.append(root.val)
                if root.left is not None:
                    queue.append(root.left)
                if root.right is not None:
                    queue.append(root.right)
            result.append(level)
        return result
        