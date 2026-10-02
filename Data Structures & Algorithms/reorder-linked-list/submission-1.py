# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return
        # 1. 找到前半段的最后一个节点
        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next
            fast = fast.next
        # 保存后半段的头节点，然后断开两半
        second = slow.next
        slow.next = None

        # 2. 反转后半段，上一题
        prev = None
        curr = second
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        # 3. 交替连接前半段和反转后的后半段
        first = head
        second = prev #反转后的链表的head
        while second is not None:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next
            first = first_next
            second = second_next
            
# I solve this problem in three steps.
# First, I use a slow pointer and a fast pointer to find the middle of the list. The slow pointer moves one step at a time, and the fast pointer moves two steps. Then I split the list into two halves.
# Second, I reverse the second half, so I can access the original nodes from the end toward the middle.
# Third, I merge the two halves by alternating nodes: one from the first half, then one from the reversed second half. Before changing the links, I save the next node in each half so I can continue.
# I modify the links in place without changing any node values. There is no need to return a new head because the first node stays the same.
# The time complexity is O(n), and the extra space complexity is O(1).

