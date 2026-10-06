# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_so_far):
            if node is None:
                return 0

            # Check whether the current node is good.
            count = 0
            if node.val >= max_so_far:
                count = 1

            # Update the maximum before visiting the children.
            max_so_far = max(max_so_far, node.val)

            # Count good nodes in both subtrees.
            left_count = dfs(node.left, max_so_far)
            right_count = dfs(node.right, max_so_far)

            return count + left_count + right_count

        return dfs(root, root.val)
# I'll use DFS and keep track of the maximum value along the current path.
#
# For each node, if its value is greater than or equal to that maximum,
# it is a good node, so I count it as one.
#
# Then I update the maximum to include the current node's value
# and pass it to the recursive calls for the left and right children.
#
# Each call returns the number of good nodes in its subtree.
# I add the current node's contribution to the counts from both subtrees.
# For an empty subtree, I return zero.
#
# I start from the root, using its value as the initial maximum.
# This ensures that the root is counted as a good node.
#
# The time complexity is O(n), because each node is visited once.
# The space complexity is O(h) for the recursion stack,
# where h is the height of the tree.


# 思路：DFS，向下传递路径最大值，向上返回 good nodes 数量。
#
# 1. 定义 dfs(node, max_so_far)：
#    - node：当前节点。
#    - max_so_far：当前节点之前，祖先路径上的最大值。
#    - 返回值：以当前节点为根的子树中的 good nodes 数量。
#
# 2. 递归终止条件：
#    - 如果 node is None，返回 0。
#
# 3. 判断当前节点是否 good：
#    - count = 0
#    - 如果 node.val >= max_so_far，设置 count = 1。
#    - 相等也算 good，比较的是所有祖先的最大值，不只是父节点。
#
# 4. 更新路径最大值：
#    - max_so_far = max(max_so_far, node.val)
#    - 对孩子来说，当前节点也属于它们的祖先路径。
#
# 5. 递归统计左右子树：
#    - left_count = dfs(node.left, max_so_far)
#    - right_count = dfs(node.right, max_so_far)
#    - 当前节点不是 good，也必须继续检查孩子。
#    - 左右分支分别维护自己的路径最大值，不会互相影响。
#
# 6. 返回当前子树的 good nodes 总数：
#    - return count + left_count + right_count
#    - 当前节点的贡献 + 左子树数量 + 右子树数量。
#
# 7. 启动递归并返回答案：
#    - return dfs(root, root.val)
#    - 根节点与自己的值比较，一定会被计入。
#
# 注意：max_so_far 是当前路径的最大值，不是整棵树的最大值。
# 时间复杂度：O(n)，每个节点访问一次。
# 空间复杂度：O(h)，递归栈深度取决于树高，最坏为 O(n)。
