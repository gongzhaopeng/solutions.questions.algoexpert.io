# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        self.heap = array
        self.buildHeap()

    # Algorithmic Beauty Bless You - O(n) time | O(1) space
    def buildHeap(self):
        for i in reversed(range(len(self.heap) // 2)):
            self.siftDown(i)

    # Algorithmic Beauty Bless You - O(logn) time | O(1) space
    def siftDown(self, i):
        while True:
            p_left = i * 2 + 1
            indices = [i, p_left, p_left + 1]
            p_min = min(filter(lambda _: _ < len(self.heap), indices), key=lambda _: self.heap[_])
            if p_min == i:
                break
            self.swap(i, p_min)
            i = p_min

    # Algorithmic Beauty Bless You - O(logn) time | O(1) space
    def siftUp(self, i):
        while i > 0:
            p_parent = (i - 1) // 2
            if self.heap[i] < self.heap[p_parent]:
                self.swap(i, p_parent)
                i = p_parent
            else:
                break

    # Algorithmic Beauty Bless You - O(1) time | O(1) space
    def peek(self):
        return self.heap[0]

    # Algorithmic Beauty Bless You - O(logn) time | O(1) space
    def remove(self):
        self.swap(0, -1)
        v_min = self.heap.pop()
        self.siftDown(0)
        return v_min

    # Algorithmic Beauty Bless You - O(logn) time | O(1) space
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
