# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # Algorithmic Beauty Bless You - O(n^2) time | O(n^2) space
    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            node = self.root
            for j in range(i, len(string)):
                node = node.setdefault(string[j], {})
            node[self.endSymbol] = True

    # Algorithmic Beauty Bless You - O(m) time | O(1) space
    def contains(self, string):
        node = self.root
        for ch in string:
            node = node.get(ch)
            if not node:
                return False
        return self.endSymbol in node
