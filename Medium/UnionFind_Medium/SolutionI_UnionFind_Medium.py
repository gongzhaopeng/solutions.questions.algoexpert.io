# Do not edit the class below except for
# the constructor and the createSet, find,
# and union methods. Feel free to add new
# properties and methods to the class.
class UnionFind:
    def __init__(self):
        self.parents = {}
        self.ranks = {}

    # Algorithmic Beauty Bless You - O(1) time | O(1) space
    def createSet(self, value):
        self.parents[value] = value
        self.ranks[value] = 0

    # Algorithmic Beauty Bless You - O(α(n))>>O(1) time | O(α(n))>>O(1) space
    def find(self, value):
        p = self.parents.get(value)
        if p is None:
            return None
        path = []
        while value != p:
            path.append(value)
            value = p
            p = self.parents[p]
        for v in path:
            self.parents[v] = p
        return p

    # Algorithmic Beauty Bless You - O(α(n))>>O(1) time | O(α(n))>>O(1) space
    def union(self, valueOne, valueTwo):
        root_one = self.find(valueOne)
        if root_one is None:
            return
        root_two = self.find(valueTwo)
        if root_two is None or root_one == root_two:
            return
        rank_one, rank_two = self.ranks[root_one], self.ranks[root_two]
        if rank_one < rank_two:
            self.parents[root_one] = root_two
        else:
            self.parents[root_two] = root_one
            if rank_one == rank_two:
                self.ranks[root_one] = rank_one + 1
