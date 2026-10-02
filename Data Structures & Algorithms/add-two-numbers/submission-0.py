# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1 = 0  # val1 = l1.val if l1 else 0

            if l2:
                val2 = l2.val
            else:
                val2 = 0  # val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            digit = total % 10  #取个位，作为当前结果节点的值
            carry = total // 10  #取整除结果，作为下一位的进位

            curr.next = ListNode(digit) #把当前结果数字添加到新链表。
            curr = curr.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next