import heapq


# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
class ContinuousMedianHandler:
    def __init__(self):
        self.left_half, self.right_half = [], []
        self.median = None

    # Algorithmic Beauty Bless You - O(logn) time | O(n) space
    def insert(self, number):
        if not self.right_half:
            self.right_half.append(number)
            self.median = number
        elif len(self.left_half) == len(self.right_half):
            if number < -self.left_half[0]:
                heapq.heappush(self.left_half, -number)
                number = -heapq.heappop(self.left_half)
            heapq.heappush(self.right_half, number)
            self.median = self.right_half[0]
        else:
            if number > self.right_half[0]:
                heapq.heappush(self.right_half, number)
                number = heapq.heappop(self.right_half)
            heapq.heappush(self.left_half, -number)
            self.median = (-self.left_half[0] + self.right_half[0]) / 2

    def getMedian(self):
        return self.median
