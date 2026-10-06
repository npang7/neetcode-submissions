# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def checkHeight(node):
            if node is None:
                return 0

            left_height = checkHeight(node.left)
            if left_height == -1:
                return -1

            right_height = checkHeight(node.right)
            if right_height == -1:
                return -1
            
            #如果左右子树都平衡，才检查当前节点
            if abs(left_height - right_height) > 1:
                return -1
            #返回当前子树高度
            return 1 + max(left_height, right_height)

        return checkHeight(root) != -1


# 当前节点是平衡的，因为高度差为 1。但检查完之后，还需要告诉父节点：
# 当前子树高度 = 1 + max(2, 1) = 3
# 父节点拿到这个 3，才能和它另一边子树的高度进行比较。

# I’ll use a recursive helper function to calculate the height of each subtree and check whether it’s balanced.
# For an empty subtree, I return zero. Otherwise, I recursively get the heights of the left and right subtrees. If either call returns negative one, that means the subtree is already unbalanced, so I return negative one immediately.
# If both subtrees are balanced, I check their height difference. If it’s greater than one, I return negative one. Otherwise, I return one plus the larger height, so the parent node can use it to check its own balance.
# Finally, the whole tree is balanced if the helper returns anything other than negative one for the root.
# The time complexity is O(n), because each node is processed at most once. The space complexity is O(h) for the recursion stack, where h is the height of the tree.

#关于return -1的传递：
# 通过递归调用的返回过程向上传递。
# 关键是：return 只结束当前这一次函数调用，不会把所有递归调用都结束。


