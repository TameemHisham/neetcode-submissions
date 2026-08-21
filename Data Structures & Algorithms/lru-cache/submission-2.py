
class Node:
    def __init__(self, key,val):
        self.key =key
        self.val = val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # Key -> Node 
        self.mostRecent = Node(0,0)
        self.leastRecent = Node(0,0)
        self.leastRecent.next, self.mostRecent.prev = self.mostRecent, self.leastRecent

    def remove(self,node): # remove node from linked list 
        nxt = node.next
        prev = node.prev 
        prev.next = nxt
        nxt.prev = prev
    def insert(self,node): # add node to right of linked list 
        prev, nxt = self.mostRecent.prev, self.mostRecent
        prev.next = node
        nxt.prev = node 
        node.next = nxt
        node.prev = prev
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key] = Node(key,value)
            self.insert(self.cache[key])
        else:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # evict least recently used 
            lru = self.leastRecent.next
            self.remove(lru)
            del self.cache[lru.key]


