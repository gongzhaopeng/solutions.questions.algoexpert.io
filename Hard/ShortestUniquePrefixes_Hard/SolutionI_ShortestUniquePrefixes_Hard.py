# Algorithmic Beauty Bless You - O(n*m) time | O(n*m) space
def shortestUniquePrefixes(strings):
    trie = Trie(strings)
    return [find_shortest_unique_prefix(_, trie) for _ in strings]


def find_shortest_unique_prefix(string, trie):
    current, i = trie.root, -1
    for i, ch in enumerate(string):
        current = current[ch]
        frequency = current['fr']
        if frequency == 1:
            break
    return string[:i + 1]


class Trie:
    def __init__(self, strings):
        self.root = {}
        for string in strings:
            self.insert(string)

    def insert(self, string):
        current = self.root
        for ch in string:
            current = current.setdefault(ch, {'fr': 0})
            current['fr'] += 1
