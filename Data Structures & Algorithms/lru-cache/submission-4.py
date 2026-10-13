class Node:
    def __init__(self,key,value):
        self.key,self.val=key,value
        self.prev,self.next = None,None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashmap = {}
        self.mru,self.lru=Node(0,0),Node(0,0)
        self.mru.next, self.lru.prev = self.lru,self.mru
    
    def add(self,node):
        prev, nxt = self.mru, self.mru.next
        prev.next= nxt.prev = node
        node.prev,node.next=prev,nxt
    
    def remove(self,node):
        prev,nxt = node.prev,node.next
        prev.next,nxt.prev = nxt,prev

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        node = Node(key,value)
        self.hashmap[key]=node
        self.add(node)

        if len(self.hashmap)>self.cap:
            lru = self.lru.prev
            self.remove(lru)
            del self.hashmap[lru.key]
