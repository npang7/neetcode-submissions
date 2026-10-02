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

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
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

        self._remove(node) #将节点从原位置移除，再放到链表末尾，表示它刚刚被使用
        self._insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            self._remove(node) #将节点从原位置移除，再放到链表末尾，表示它刚刚被使用
            self._insert(node)
            return

        node = Node(key, value) #新建node
        self.cache[key] = node #保存到字典
        self._insert(node) #加入链表末尾
        #检查容量
        if len(self.cache) > self.capacity:
            lru = self.head.next  #head是一个 dummy node，本身不存缓存数据，
                                    #head.next 是第一个真实节点
            self._remove(lru)       # 从链表中摘掉
            del self.cache[lru.key] # 从字典中删除

