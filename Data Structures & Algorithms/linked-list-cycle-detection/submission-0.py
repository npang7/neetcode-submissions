# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            # 慢指针走一步
            slow = slow.next

            # 快指针走两步
            fast = fast.next
            fast = fast.next

            # 判断是否到达同一个节点
            if slow is fast:
                return True

        return False

#让两个指针沿着链表走，一个每次走一步，另一个每次走两步。没有环就会走到尽头；有环就会在环里相遇。

# 如果只靠“遇到 None”判断呢？
# 对于没有环的链表，确实可以一直走，遇到 None 就返回 False。
# 但有环的链表永远不会遇到 None，程序就会一直循环，无法返回 True。所以还需要通过快慢指针相遇来识别有环；

# I use two pointers, slow and fast. Both start at the head.
# In each iteration, slow moves one step and fast moves two steps. After moving them, I check whether they point to the same node.
# If there is a cycle, the fast pointer will eventually catch up with the slow pointer, so I return true.
# If fast or fast.next is None, the list has an end, so there is no cycle, and I return false.
# The time complexity is O(n), and the extra space complexity is O(1).
