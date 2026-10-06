# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from collections import deque

class Solution:  #层序遍历（Level Order Traversal)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        result = []
        queue = deque()
        queue.append(root) #deque：双端队列（double-ended queue），FIFO

        while queue: #只要队列还有节点，就继续
            level_size = len(queue) #上次加了几个孩子就有几个节点
            level = [] #用于记录这一层的val的列表，后面会把他append到result

            for i in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            result.append(level)

        return result