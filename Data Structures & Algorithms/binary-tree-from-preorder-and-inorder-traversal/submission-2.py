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
                return None
            root_value = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_value)

            mid = inorder_val_to_idx[root_value]
            root.left = build(left, mid-1)
            root.right = build(mid+1,right)
            return root
        return build(0,len(preorder)-1)