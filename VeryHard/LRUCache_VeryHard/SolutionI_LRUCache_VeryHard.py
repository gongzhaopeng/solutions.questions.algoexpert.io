# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.cache = {}
        self.size = 0
        self.lru_dll = DoublyLinkedList()

    # Algorithmic Beauty Bless You - O(1) time | O(1) space
    def insertKeyValuePair(self, key, value):
        node = self.cache.get(key)
        if not node:
            if self.size < self.maxSize:
                self.size += 1
                node = Node(key, value)
            else:
                node = self.lru_dll.tail
                del self.cache[node.key]
                node.key = key
            self.cache[key] = node
        node.value = value
        self.update_most_recent(node)

    # Algorithmic Beauty Bless You - O(1) time | O(1) space
    def getValueFromKey(self, key):
        node = self.cache.get(key)
        if node:
            self.update_most_recent(node)
            return node.value
        return None

    # Algorithmic Beauty Bless You - O(1) time | O(1) space
    def getMostRecentKey(self):
        return self.lru_dll.head.key if self.lru_dll.head else None

    def update_most_recent(self, node):
        self.lru_dll.setHead(node)


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = self.tail = node
            return
        if self.head is node:
            return
        if node.prev:
            node.prev.next = node.next
        if self.tail is node:
            self.tail = node.prev
        elif node.next:
            node.next.prev = node.prev
        node.prev, node.next, self.head.prev, self.head = None, self.head, node, node
