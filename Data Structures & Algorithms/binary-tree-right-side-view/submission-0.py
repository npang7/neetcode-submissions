# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = collections.deque()
        result = []
        queue.append(root)

        while queue:
            level_len = len(queue)
            for i in range(level_len):
                root = queue.popleft()
                if i == level_len - 1:
                    result.append(root.val)
                if root.left is not None:
                    queue.append(root.left)
                if root.right is not None:
                    queue.append(root.right)
        return result