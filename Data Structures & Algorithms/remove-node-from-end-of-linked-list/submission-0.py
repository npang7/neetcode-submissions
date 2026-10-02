# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        slow = dummy
        fast = dummy

        # fast 先走 n + 1 步
        for i in range(n + 1):
            fast = fast.next

        # 两个指针一起走，保持间距
        while fast is not None:
            slow = slow.next
            fast = fast.next

        # slow 指向待删除节点的前一个节点！！
        node_to_remove = slow.next
        node_after = node_to_remove.next
        slow.next = node_after

        return dummy.next