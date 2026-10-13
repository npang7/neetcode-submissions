"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        # 原节点对象 → 新节点对象
        old_to_new = {}  

        # 返回 original 对应的新节点
        def dfs(original):
            # 已经创建过副本，直接返回它
            if original in old_to_new:
                return old_to_new[original]

            # 创建当前节点的副本，邻居列表暂时为空
            copy = Node(original.val)   #！！！
            # 先记录对应关系，再递归处理邻居
            old_to_new[original] = copy    #！！！

            # 复制邻居，并连接到当前副本
            for neighbor in original.neighbors:
                copied_neighbor = dfs(neighbor)    #！！！
                copy.neighbors.append(copied_neighbor)  #！！！

            return copy

        return dfs(node)   #cloneGraph 最终返回复制后的图的起始节点

# 中文思路清单（DFS + 原节点到新节点的映射）
#
# 1. 理解输入和需要返回的结果。
#    - node 是原图的起始节点对象，不是邻接表。
#    - Optional['Node'] 表示节点对象或者 None。
#    - 每个节点有 val 和 neighbors 两个属性。
#    - neighbors 保存邻居节点对象，不是整数编号。
#    - 最终返回新图的起始节点，通过它可以访问整个新图。
#
# 2. 处理空图。
#    - 如果 node is None，直接返回 None。
#
# 3. 创建 old_to_new 字典。
#    - 键：原节点对象。
#    - 值：对应的新节点对象。
#    - 用来避免重复创建节点，也用来找到已有副本并建立连接。
#    - old_to_new 在各次 DFS 调用之间共享。
#
# 4. 调用 dfs(node)，从原图的起始节点开始复制。
#    - dfs(original) 的任务：返回 original 对应的新节点。
#    - original 是当前正在处理的原节点。
#
# 5. 进入 DFS 后，先检查当前节点是否已经有副本。
#    - 如果 original in old_to_new，直接返回 old_to_new[original]。
#    - 不再创建新节点，也不继续递归处理它。
#    - 这可以避免在无向图的相邻节点之间无限递归。
#
# 6. 如果没有副本，就创建并立即记录。
#    - copy = Node(original.val)：创建值相同的新节点。
#    - 新节点的 neighbors 暂时是空列表。
#    - old_to_new[original] = copy：保存原节点与新节点的对应关系。
#    - 必须先存入字典，再递归访问邻居。
#    - 这样邻居再次访问到当前原节点时，就能拿到已有副本。
#
# 7. 遍历原节点的邻居，建立新节点之间的连接。
#    - for neighbor in original.neighbors：依次处理每个原邻居。
#    - copied_neighbor = dfs(neighbor)：取得邻居对应的新节点。
#    - 如果邻居已有副本，DFS 直接返回它；否则创建并处理它。
#    - copy.neighbors.append(copied_neighbor)：把新邻居加入新节点的邻居列表。
#
# 8. 当前节点的邻居处理完成后，返回 copy。
#    - 上一层拿到 copy 后，将它加入自己的新节点的邻居列表。
#    - 最外层的 return dfs(node) 返回新图的起始节点。
#    - 只需要返回一个起始节点，因为图是连通的。
#
# 9. 容易混淆的地方。
#    - 深拷贝要求创建全新的节点，连接也必须指向新节点。
#    - 不能把原来的 neighbor 直接加入 copy.neighbors。
#    - 已有副本时，要返回副本对象，不能只写 return。
#      上一层需要这个新节点对象来建立连接。
#    - 字典中出现一个节点，表示它的副本已经创建，
#      不一定表示副本的邻居列表已经全部填完。
#    - 提前返回已有副本是安全的，因为引用的是同一个新节点对象，
#      后续添加的邻居也会体现在这个对象上。
#    - 不需要额外的 visited 集合，old_to_new 已经记录了哪些节点创建过副本。
#    - 原图不会被修改，也不要在递归结束后删除字典中的对应关系。
#    - 一个没有邻居的节点仍然需要复制，只是邻居循环不会执行。
#    - 函数返回 Node 对象；题目中的邻接表是平台展示图的方式。
#
# 10. 时间和空间复杂度。
#     - 假设图有 V 个节点、E 条边。
#     - 时间复杂度：O(V + E)。
#       每个节点只创建一次，遍历所有节点的邻居列表。
#     - 辅助空间复杂度：O(V)。
#       字典保存 V 个对应关系，递归栈最坏需要 O(V)。
#     - 如果包含输出的新图，总空间为 O(V + E)。
#
# 快速记忆思路
# 查字典 → 创建副本 → 先存字典 → 复制邻居并连接 → 返回副本。
# DFS 给我一个原节点，我返回它对应的新节点。
#
# 口语讲述思路
#
# I'll use depth-first search and a dictionary to clone the graph.
# The dictionary maps each original node to its copy.
#
# First, if the input node is None, I return None.
# Otherwise, I start DFS from that node.
#
# In DFS, I first check if the node already has a copy.
# If it does, I return the existing copy.
#
# Otherwise, I create a new node with the same value
# and store it in the dictionary before visiting its neighbors.
# This prevents infinite recursion when I reach the same node again.
#
# Then I go through each neighbor of the original node.
# I call DFS to get that neighbor's copy
# and add it to the new node's neighbors list.
#
# After processing all the neighbors, I return the new node.
# The main function returns the copy of the starting node.
# Since the graph is connected, I can reach the entire copied graph from it.
#
# Every node is new, and every neighbor reference points to a copied node,
# so the result is a deep copy.
#
# The time complexity is O(V + E),
# where V is the number of nodes and E is the number of edges.
# The auxiliary space complexity is O(V)
# for the dictionary and the recursion stack.
# Including the copied graph, the total space is O(V + E).
