# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next  # 保存原来的下一个节点
            curr.next = prev       # 反转当前节点的指向
            prev = curr            # prev 移到当前节点
            curr = next_node       # curr 移到原来的下一个节点

        return prev