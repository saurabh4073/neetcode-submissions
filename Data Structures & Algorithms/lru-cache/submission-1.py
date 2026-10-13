class Node:
    def __init__(self,key,value):
        self.key= key
        self.value= value
        self.prev=self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.lru,self.mru=Node(0,0),Node(0,0)
        self.lru.next,self.mru.prev=self.mru,self.lru
    
    def remove(self, node):
        prev,nxt = node.prev,node.next
        prev.next,nxt.prev = nxt,prev

    def insert(self,node):
        prev,nxt = self.mru.prev,self.mru
        prev.next= nxt.prev = node
        node.next,node.prev = nxt,prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.capacity:
            lru = self.lru.next
            self.remove(lru)
            del self.cache[lru.key]




