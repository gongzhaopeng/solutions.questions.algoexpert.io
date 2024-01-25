# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = [float('inf'), float('-inf'), None]

    # Algorithmic Beauty Bless You - O(1) time | O(1) space
    def peek(self):
        return self.stack[-1]

    # Algorithmic Beauty Bless You - O(1) time | O(1) space
    def pop(self):
        v = self.peek()
        self.stack[-3:] = []
        return v

    # Algorithmic Beauty Bless You - O(1) time | O(1) space
    def push(self, number):
        self.stack.extend([min(self.stack[-3], number), max(self.stack[-2], number), number])

    # Algorithmic Beauty Bless You - O(1) time | O(1) space
    def getMin(self):
        return self.stack[-3]

    # Algorithmic Beauty Bless You - O(1) time | O(1) space
    def getMax(self):
        return self.stack[-2]
