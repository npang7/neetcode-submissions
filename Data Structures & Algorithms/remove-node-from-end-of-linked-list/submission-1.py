class Solution:
    def removeNthFromEnd(
        self, head: ListNode | None, n: int
    ) -> ListNode | None:
        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        # 快指针先走 n 步
        for _ in range(n):
            fast = fast.next

        # 保持间隔，一起移动，直到 fast 到达最后一个节点
        while fast.next:
            slow = slow.next
            fast = fast.next

        # slow 指向待删除节点的前一个节点
        slow.next = slow.next.next

        return dummy.next