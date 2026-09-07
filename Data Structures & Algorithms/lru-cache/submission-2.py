class Node:
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheKey = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    
    def insert(self, node):
        prev = self.right.prev
        node.prev = prev
        node.next = self.right
        prev.next = node
        self.right.prev = node
        
        

    def get(self, key: int) -> int:
        if key in self.cacheKey:
            self.remove(self.cacheKey[key])
            self.insert(self.cacheKey[key])
            return self.cacheKey[key].value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cacheKey:
            self.remove(self.cacheKey[key])
        self.cacheKey[key] = Node(key, value)
        self.insert(self.cacheKey[key])
        if len(self.cacheKey) > self.capacity:
            LRU = self.left.next
            self.remove(LRU)
            del self.cacheKey[LRU.key]

        
