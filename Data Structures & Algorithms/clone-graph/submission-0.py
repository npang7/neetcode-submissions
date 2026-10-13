"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        old_to_new = {}
        def dfs(original):
            if original in old_to_new:
                return old_to_new[original]
            
            copy = Node(original.val)
            old_to_new[original] = copy

            for neighbor in original.neighbors:
                copied_neighbor = dfs(neighbor)
                copy.neighbors.append(copied_neighbor)
            return copy
        return dfs(node)