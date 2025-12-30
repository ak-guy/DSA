"""
we will use Doubly Linked List and dictionary to solve this problem
"""


class Node:
    def __init__(self, key, value):
        self.key = key  # integer
        self.value = value  # Node
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)  # First Node
        self.tail = Node(-1, -1)  # Second Node
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def get(self, key: int) -> int:
        if key in self.dic:
            val = self.dic[key]
            self.removeFromList(val)
            self.addToHead(val)
            return val.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            val = self.dic[key]
            self.removeFromList(val)
            self.addToHead(val)
            val.value = value
        else:
            if self.length >= self.capacity:
                self.removeFromTail()
            node = Node(key, value)
            self.dic[key] = node
            self.addToHead(node)

    def removeFromList(self, node):
        """will be used to remove a node from DLL then later to insert at head"""
        node.prev.next = node.next
        node.next.prev = node.prev
        self.length -= 1

    def addToHead(self, node):
        """will be used to add a node after head(making it recently used element) -> head.next = node"""
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node
        self.length += 1

    def removeFromTail(self):
        """this will be used to remove a node previous to tail, to make DLL follow LRU cache logic"""
        tail_node = self.tail.prev
        del self.dic[tail_node.key]
        self.removeFromList(tail_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
