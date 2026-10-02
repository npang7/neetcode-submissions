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
            #不要忘记是ListNode()！！！因为是新建的node，本来没有，不能只是改val！
            curr = curr.next    #新链表往后继续走

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next  # the head of the new linked list


# Since the digits are stored in reverse order, I can add the numbers digit by digit, starting from the heads of the two lists.
# I use a dummy node and a tail pointer to build the result list. I also keep a carry, which starts at zero.
# At each step, I add the current digits from both lists and the carry. If one list has already ended, I use zero for its digit.
# The new digit is the sum modulo ten, and the new carry is the sum divided by ten using integer division.
# I create a node with the new digit, append it to the result, and move the tail pointer forward. I also advance the input pointers if they are not null.
# I continue while either list has remaining nodes or the carry is nonzero. This ensures that I include any final carry.
# Finally, I return dummy.next, which is the head of the result list.
# The time complexity is O(max(m, n)), where m and n are the lengths of the input lists. The extra space is O(1), excluding the output list.