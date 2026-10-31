# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        first = head
        second = slow.next
        slow.next = None #别忘记！！

        prev = None
        current = second
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        second = prev

        dummy = ListNode(0 , first)
        while first and second:
            first_next = first.next 
            first.next = second
            second_next = second.next
            second.next = first_next
            first = first_next
            second = second_next

             