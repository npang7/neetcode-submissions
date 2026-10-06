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

        while queue: # ！= “while queue is not None”，
                         #因为空队列也不是none，但会一直在循环里！！
                         # “while queue”代表是空队列的时候就结束
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


# I’ll use BFS with a queue, implemented using a deque.
# If the root is None, I return an empty list. Otherwise, I add the root to the queue.
# While the queue is not empty, I record its current size, which tells me how many nodes are in the current level. I also create a list called level to store their values.
# I then use a for loop to process exactly that many nodes. For each node, I remove it from the front of the queue and add its value to level. Then I add its left and right children to the back of the queue, if they exist.
# After processing the entire level, I append level to result. Once the queue is empty, I return result.
# The time complexity is O(n), since each node is processed once. The extra space complexity is O(n) in the worst case for the queue.
