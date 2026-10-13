class Node:
    def __init__(self,key, value):
        self.key, self.value= key,value
        self.prev, self.next= None,None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashmap = {} # key: value is pointer
        self.lru, self.mru = Node(0,0), Node(0,0)
        self.lru.next,self.mru.prev=self.mru,self.lru

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt,prev

    #insert at the MRU
    def insert(self, node):
        prev, nxt = self.mru.prev, self.mru
        prev.next=nxt.prev= node
        node.next,node.prev= nxt, prev

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        node = Node(key,value)
        self.insert(node)
        self.hashmap[key]=node

        if len(self.hashmap)>self.cap:
            lru = self.lru.next
            self.remove(lru)
            del self.hashmap[lru.key]
