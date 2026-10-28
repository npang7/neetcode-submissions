class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        last = self.right.prev
        last.next = node
        node.prev = last
        node.next = self.right
        self.right.prev = node
    
    def remove(self,node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        value = node.val

        self.remove(node)
        self.insert(node)

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            return
        
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            oldest = self.left.next
            self.remove(oldest)
            del self.cache[oldest.key]

        #return #可以省略
        
