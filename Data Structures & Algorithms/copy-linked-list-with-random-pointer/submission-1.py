"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {None: None} #提前记录： 原指针如果是 None，复制后的指针也应该是 None。

        # 第一遍：为每个原节点创建对应的新节点
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val) #Node(curr.val) 创建一个新节点，保存与当前原节点相同的值。
            curr = curr.next

        # 第二遍：设置新节点的 next 和 random
        curr = head
        while curr:
            new_node = old_to_new[curr]
            new_node.next = old_to_new[curr.next]
            new_node.random = old_to_new[curr.random]
            curr = curr.next

        return old_to_new[head] #head 是原链表的头节点，而 old_to_new[head] 是它对应的新节点，所以返回的就是新链表的头节点

# I’ll use a "hash map" to map each original node to its copy. I use the nodes themselves as keys because different nodes may have the same value.
# I’ll make two passes through the list.
# In the first pass, I create a new node with the same value for each original node and store the mapping in the hash map. At this point, the new nodes are not connected yet.
# In the second pass, I set the next and random pointers for each copied node. I look up the original node’s next and random targets in the hash map and connect the copied node to their corresponding copies.
# For example, if node A’s random pointer points to node B, the copied A’s random pointer should point to the copied B.
# I create all the nodes first because a random pointer may point to a node later in the list. I also map None to None to handle null pointers and an empty list.
# Finally, I return the copy of the original head.
# The time complexity is O(n), since I traverse the list twice. The extra space complexity is O(n) for the hash map.