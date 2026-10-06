# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def max_depth(root):
            if root is None:
                return 0

            left_depth = max_depth(root.left)
            right_depth = max_depth(root.right)

            # 更新经过当前节点的最长路径长度 #比maxdepth多了这部分
            # 更新diameter这个对象属性
            self.diameter = max(
                self.diameter,
                left_depth + right_depth
            )

            # 返回以当前节点为根的子树的最大深度
            return 1 + max(left_depth, right_depth)

        max_depth(root)
        return self.diameter

# Diameter of Binary Tree 思路清单
#
# 核心口诀：
# 左右深度相加，更新直径；较大深度加一，返回父节点。
#
# 1. 理解题意
#    - 直径：任意两个节点之间最长路径的边数。
#    - 计算的是边数，不是节点数。
#    - 最长路径不一定经过根节点，所以要检查每个节点。
#
# 2. 核心思路：DFS + 后序遍历
#    - 先计算左子树深度。
#    - 再计算右子树深度。
#    - 最后处理当前节点。
#    - 空树深度为 0，叶子节点深度为 1。
#
# 3. 递归函数 depth(node) 做两件事
#
#    A. 更新答案：
#       经过当前节点的最长路径：
#       左子树最深节点 -> 当前节点 -> 右子树最深节点。
#
#       路径边数 = left_depth + right_depth
#       self.diameter = max(self.diameter, left_depth + right_depth)
#
#       为什么不加 1？
#       左子树深度恰好等于从当前节点到左侧最深节点的边数。
#       右侧同理，因此直接相加即可。
#
#    B. 返回深度：
#       return 1 + max(left_depth, right_depth)
#
#       为什么只取一边？
#       父节点向下延伸路径时，只能选择一条分支，不能分叉。
#       加 1 是把当前节点计入子树深度。
#
# 4. 实现顺序
#    - 初始化 self.diameter = 0。
#    - 定义 depth(node)，空节点返回 0。
#    - 递归获取左右子树深度。
#    - 用左右深度之和更新直径。
#    - 返回较大深度 + 1。
#    - 调用 depth(root)，最后返回 self.diameter。
#
# 5. 易错点
#    - depth() 返回的是子树深度，不是直径。
#    - depth(root) 得到的是整棵树的深度，不能直接作为答案。
#    - 更新直径用 left_depth + right_depth。
#    - 返回深度用 1 + max(left_depth, right_depth)。
#    - 只有一个节点时：深度为 1，直径为 0。
#    - 节点的 val 不影响答案，只看树的结构。
#
# 6. 复杂度
#    - 时间：O(n)，每个节点处理一次。
#    - 空间：O(h)，递归栈取决于树高。
#      平衡树为 O(log n)，退化成链表时为 O(n)。


# I’ll use a recursive depth-first search.

# For each node, I first calculate the depths of its left and right subtrees. The depth of an empty subtree is zero.

# The longest path through the current node connects the deepest node in the left subtree to the deepest node in the right subtree. Its length in edges is the sum of the two subtree depths.

# I use this sum to update the maximum diameter. Since I check every node, the longest path doesn’t have to pass through the root.

# Then I return one plus the larger subtree depth to the parent. I only take one side because a path extending from the parent cannot branch.

# Finally, I return the maximum diameter.

# The time complexity is O(n), since each node is visited once. The space complexity is O(h) for the recursion stack, where h is the height of the tree.