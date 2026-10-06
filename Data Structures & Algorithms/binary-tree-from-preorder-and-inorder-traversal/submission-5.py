# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_val_to_idx = {}
        for index, value in enumerate(inorder):
            inorder_val_to_idx[value] = index
        self.pre_idx = 0

        def build(left, right):
            if left > right:
                return None #记得写：什么时候结束递归呢？

            root_value = preorder[self.pre_idx]
            self.pre_idx += 1

            root = TreeNode(root_value)

            mid = inorder_val_to_idx[root_value]
            root.left = build(left, mid-1)
            root.right = build(mid+1,right)
            return root
        return build(0,len(preorder)-1)


# I'll use recursion to rebuild the tree.
# Preorder visits the root first, followed by the left and right
# subtrees. So I'll keep an index into preorder to read the next
# root value.

# I'll also build a hash map that maps each value to its index
# in inorder.

# Each recursive call handles a range of the inorder array. !!!
# If the range is empty, I return None.

# Otherwise, I create the root using the next preorder value
# and move the preorder index forward.

# Then I find the root's position in inorder. The values before
# it belong to the left subtree, and the values after it belong
# to the right subtree, within the current range.

# I recursively build the left subtree first, then the right
# subtree, and connect them to the root.

# This order matches preorder traversal, so the index always
# points to the next subtree's root.

# Each node is processed once, so the time complexity is O(n).
# The extra space is O(n) for the hash map and recursion stack.

# Construct Binary Tree from Preorder and Inorder Traversal
# 方法：哈希表 + 前序指针 + 递归
#
# 1. 记住遍历顺序：
#    preorder：根 → 左子树 → 右子树
#    inorder：左子树 → 根 → 右子树
#
# 2. 建立哈希表 inorder_val_to_idx：
#    节点值 → 它在原中序数组中的下标。
#
# 3. 初始化 self.pre_idx = 0：
#    记录前序数组中下一个还没使用的数字的位置。
#    所有递归调用共同使用这个指针。
#
# 4. 定义 build(left, right)：
#    构建中序数组下标 left 到 right 对应的子树。
#    范围包含两端；返回建好的子树根节点。
#
# 5. 如果 left > right：
#    当前范围为空，返回 None。
#    不创建节点，也不移动前序指针。
#
# 6. 从 preorder[self.pre_idx] 取出当前根的值：
#    随后 self.pre_idx += 1，并创建根节点。
#
# 7. 用哈希表找到根的中序位置 mid：
#    mid、left、right 都是原中序数组中的下标。
#
# 8. 递归构建左子树并连接：
#    root.left = build(left, mid - 1)
#
# 9. 递归构建右子树并连接：
#    root.right = build(mid + 1, right)
#
# 10. 必须先建完整个左子树，再建右子树：
#     创建节点的顺序与前序遍历一致， !!!!!
#     所以下一个未使用的前序值就是当前子树的根。
#
# 11. 返回 root：
#     此时 root 已经连接好了左右子树。
#
# 12. 从整个中序范围开始：
#     return build(0, len(inorder) - 1)
#
# 时间复杂度：O(n)，每个节点处理一次。
# 额外空间：O(n)，哈希表 O(n)，递归栈 O(h)。
# h 是树高，最坏情况下 h = n。
