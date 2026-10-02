class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #dictionary // hash map

        self.head = Node() # dummy
        self.tail = Node() # dummy

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node): #改变前节点的next指针，后节点的prev指针
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert(self, node): #把节点插到 tail 前面
        prev_node = self.tail.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self._remove(node) #将节点从原位置移除
        self._insert(node) #再放到链表末尾，表示它刚刚被使用

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value   #修改value

            self._remove(node) #将节点从原位置移除，再放到链表末尾，表示它刚刚被使用
            self._insert(node)
            return

        #如果这个node不在cache里
        node = Node(key, value) #新建node
        self.cache[key] = node #保存到字典
        self._insert(node) #加入链表末尾

        #检查容量，如果超出，就移除head node
        if len(self.cache) > self.capacity:
            lru = self.head.next  #head是一个 dummy node，本身不存缓存数据，
                                    #head.next 是第一个真实节点
            self._remove(lru)       # 从链表中摘掉
            del self.cache[lru.key] # 从字典中删除
# LRU Cache 思路清单
#
# 字典找节点，双向链表排顺序；用过移到尾，满了删掉头。
#
# 1. 数据结构
#    - Hash Map：按 key 快速找到节点。
#      self.cache = {}，保存 key -> Node 对象。
#    - Doubly Linked List：维护使用顺序。
#      从 head 到 tail：最久没使用 -> 最近使用。
#    - Node 包含：key、val、prev、next。
#      保存 key 是为了淘汰时删除字典记录。
#
# 2. 初始化
#    - 保存 capacity。
#    - 创建空字典 self.cache。
#    - 创建 dummy 节点 head 和 tail，并连接：
#      self.head.next = self.tail
#      self.tail.prev = self.head
#    - dummy 节点不存进字典，不计入容量。
#
# 3. _remove(node)：从链表中摘掉节点
#    prev_node = node.prev
#    next_node = node.next
#    prev_node.next = next_node
#    next_node.prev = prev_node
#
#    注意：只调整链表连接，不删除字典记录。
#
# 4. _insert(node)：插到 tail 前面，成为最近使用的节点
#    prev_node = self.tail.prev
#    prev_node.next = node
#    node.prev = prev_node
#    node.next = self.tail
#    self.tail.prev = node
#
# 5. get(key)：找 -> 移 -> 返回
#    - key 不存在：返回 -1。
#    - key 存在：
#      node = self.cache[key]
#      self._remove(node)
#      self._insert(node)
#      return node.val
#
# 6. put(key, value)
#    - key 已存在：
#      找到节点 -> 更新 val -> 摘掉 -> 插到尾部 -> return。
#    - key 不存在：
#      创建 Node(key, value) -> 存进字典 -> 插到尾部。
#    - 新增后，如果 len(self.cache) > self.capacity：
#      lru = self.head.next
#      self._remove(lru)
#      del self.cache[lru.key]
#
# 7. 关键位置
#    - self.head.next：最久没使用的真实节点（LRU）。
#    - self.tail.prev：最近使用的真实节点（MRU）。
#
# 8. 易错点
#    - 字典和链表引用的是同一个 Node 对象。
#    - 成功 get、更新 put、新增 put，都要刷新使用顺序。
#    - 移动节点：remove + insert，保留字典记录。
#    - 淘汰节点：从链表和字典中同时删除。
#    - 更新已有 key 不增加节点数量。
#
# 9. 复杂度
#    - get / put：平均 O(1)。
#    - 空间：O(capacity)。
