# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, lower, upper):
            if node is None:
                return True

            # The current value must be strictly within the bounds.
            if node.val <= lower or node.val >= upper:
                return False

            # Update the upper bound for the left subtree.
            left_valid = dfs(node.left, lower, node.val)
            if not left_valid:
                return False

            # Update the lower bound for the right subtree.
            right_valid = dfs(node.right, node.val, upper)

            return right_valid #为什么可以直接返回右边的结果？因为执行到这里时：
                                    # 1. 当前节点已经通过范围检查。
                                    # 2. 左子树已经返回 True。
                                    # 3. 只剩右子树决定最终结果。
        return dfs(root, float("-inf"), float("inf")) #第一次检查：-无穷到无穷
# I'll use DFS and pass down a lower and an upper bound for each node.
# This lets me check the constraints from all ancestors, not just the parent.
#
# For an empty subtree, I return True.
# If the current value is less than or equal to the lower bound,
# or greater than or equal to the upper bound, I return False.
# The comparisons are strict because duplicate values are not allowed.
#
# For the left subtree, I keep the lower bound
# and use the current node's value as the new upper bound.
# If the left subtree is invalid, I return False immediately.
#
# For the right subtree, I use the current node's value as the new lower bound
# and keep the upper bound.
# I return its result, since the current node and left subtree are already valid.
#
# I start from the root with negative infinity and positive infinity,
# because the root has no restrictions from ancestors.
#
# The time complexity is O(n), since each node is checked at most once.
# The space complexity is O(h) for the recursion stack,
# where h is the height of the tree.

# 思路：DFS，向下传递允许的取值范围，向上返回子树是否合法。
#
# 1. 定义 dfs(node, lower, upper)：
#    - node：当前节点。
#    - lower：严格下界，当前值必须大于它。
#    - upper：严格上界，当前值必须小于它。
#    - 返回值：当前整棵子树是否合法，True 或 False。
#
# 2. 递归终止条件：
#    - 如果 node is None，返回 True。
#    - 空子树没有节点违反 BST 规则。
#
# 3. 检查当前节点：
#    - 合法条件：lower < node.val < upper。
#    - 如果 node.val <= lower or node.val >= upper，返回 False。
#    - 违反任意一个边界就不合法，所以用 or，不是 and。
#    - 等于边界也不合法，因此重复值不允许。
#
# 4. 检查左子树：
#    - left_valid = dfs(node.left, lower, node.val)
#    - 左子树必须小于当前节点，所以更新上界为 node.val。
#    - 保留原下界，继续遵守祖先的限制。
#    - 如果 not left_valid，立即返回 False。
#
# 5. 检查右子树：
#    - right_valid = dfs(node.right, node.val, upper)
#    - 右子树必须大于当前节点，所以更新下界为 node.val。
#    - 保留原上界，继续遵守祖先的限制。
#
# 6. 返回 right_valid：
#    - 此时当前节点和左子树已经通过检查。
#    - 所以右子树的结果决定当前整棵子树是否合法。
#
# 7. 启动递归：
#    - return dfs(root, float("-inf"), float("inf"))
#    - 根节点没有祖先限制，初始范围为负无穷到正无穷。
#
# 注意：检查的是所有祖先的限制，不能只比较当前节点和直接孩子。
# 时间复杂度：O(n)，每个节点最多检查一次。
# 空间复杂度：O(h)，递归栈深度取决于树高，最坏为 O(n)。


