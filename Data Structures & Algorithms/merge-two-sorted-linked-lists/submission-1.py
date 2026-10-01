# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() #创建一个新的链表节点，并用变量 dummy 指向它
        tail = dummy    #合并开始时，结果链表还没有任何节点。
                        #我们先放一个辅助节点，就有了一个可以接上其他节点的起点。

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                # 接上 list1 的当前节点
                tail.next = list1

                # list1 移到下一个节点
                list1 = list1.next
            else:
                # 接上 list2 的当前节点
                tail.next = list2

                # list2 移到下一个节点
                list2 = list2.next

            # tail 移到刚接上的节点
            tail = tail.next

        # 接上剩余节点
        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
# I use a dummy node as the starting point of the merged list, and a tail pointer to track the last node.
# While both lists have nodes remaining, I compare their current values. I connect the smaller node to the tail, then move forward in the list I took it from. After that, I move the tail to the node I just added.
# Once one list is empty, I connect the remaining part of the other list to the tail, because it is already sorted.
# Finally, I return dummy.next, which is the head of the merged list.
# The time complexity is O(m + n), where m and n are the lengths of the two lists. The extra space complexity is O(1), because I reuse the existing nodes.
