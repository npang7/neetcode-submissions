# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        count = 0

        while current is not None or stack:
            # 一直向左走，把沿途的节点保存到栈中
            while current is not None:
                stack.append(current)
                current = current.left

            # 左边已经走完，访问当前应该处理的节点
            current = stack.pop() #栈是后进先出的，先pop最小的
            count += 1

            # 中序遍历中的第 k 个节点，就是第 k 小的节点
            if count == k:
                return current.val

            # 当前节点访问完毕，接着处理它的右子树
            current = current.right

# Since this is a binary search tree, an inorder traversal visits
# the node values in ascending order.
# So the kth node I visit will contain the kth smallest value.

# I use a stack to perform an iterative inorder traversal.
# First, I keep moving left and push each node onto the stack.

# Once I reach a null node, I pop the top node from the stack.
# This is the next node to visit in ascending order.

# I decrease a counter each time I visit a node.
# When the counter reaches zero, I return that node's value.

# Otherwise, I move to its right subtree and repeat the process.

# The time complexity is O(h + k), where h is the tree height.
# In the worst case, it is O(n).
# The space complexity is O(h) for the stack.

# Kth Smallest Integer in BST — 思路清单

# 1. 理解 BST 的性质：
#    每个节点的左子树中，所有值都比当前节点小。
#    每个节点的右子树中，所有值都比当前节点大。
#    每棵子树也满足这个规则。

# 2. 利用中序遍历：
#    中序遍历的顺序是：左子树 → 当前节点 → 右子树。
#    因此，BST 的中序遍历结果是从小到大排列的。
#    第 k 个被访问的节点，就是第 k 小的节点。

# 3. 初始化变量：
#    stack：保存之后需要回来访问的节点。
#    current：指向接下来要进入的节点。
#    remaining = k：距离答案还需要访问多少个节点。

# 4. 一直向左走：
#    把 current 放入栈，再移动到 current.left。
#    重复这个过程，直到 current 为 None。

# 5. 弹出并访问节点：
#    用 stack.pop() 取出栈顶节点。
#    此时这个节点就是中序遍历中下一个应该访问的节点。
#    每访问一个节点，就让 remaining 减 1。

# 6. 判断是否找到答案：
#    如果 remaining == 0，说明当前节点是第 k 小。
#    直接返回 current.val。

# 7. 进入右子树：
#    让 current = current.right。
#    下一轮继续向左走，再弹出并访问节点。

# 8. 外层循环条件：
#    current 不为空：还有子树需要进入。
#    stack 不为空：还有保存的节点需要回来访问。
#    因此使用：while current is not None or stack。

# 9. 复杂度：
#    n 是节点数，h 是树的高度。
#    时间复杂度：O(h + k)，最坏 O(n)。
#    空间复杂度：O(h)，用于保存栈中的节点。