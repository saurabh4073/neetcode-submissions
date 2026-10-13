class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left,self.right = None,None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.mru,self.lru = Node(0,0),Node(0,0)
        self.mru.right,self.lru.left=self.lru,self.mru

    def add(self,node):
        prev, nxt = self.mru, self.mru.right
        prev.right=nxt.left = node
        node.left,node.right= prev,nxt
    
    def remove(self,node):
        prev,nxt = node.left,node.right
        prev.right,nxt.left= nxt,prev

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        node = Node(key,value)
        self.add(node)
        self.hashmap[key]=node

        if len(self.hashmap)>self.capacity:
            lru = self.lru.left
            self.remove(lru)
            del self.hashmap[lru.key]
