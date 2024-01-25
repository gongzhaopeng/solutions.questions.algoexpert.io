# Algorithmic Beauty Bless You - O(n*m) time | O(n*m) space
def longestMostFrequentPrefix(strings):
    trie = Trie(strings)
    return trie.lmf_prefix_holder[:trie.lmf_prefix_len]


class Trie:
    def __init__(self, strings):
        self.root = {}
        self.lmf_prefix_freq, self.lmf_prefix_len, self.lmf_prefix_holder = 0, 0, None
        for string in strings:
            self.insert(string)

    def insert(self, string):
        current = self.root
        for i, ch in enumerate(string):
            current = current.setdefault(ch, {'fr': 0})
            updated_freq = current['fr'] + 1
            current['fr'] = updated_freq
            if updated_freq > self.lmf_prefix_freq or (
                    updated_freq == self.lmf_prefix_freq and i + 1 > self.lmf_prefix_len):
                self.lmf_prefix_freq, self.lmf_prefix_len, self.lmf_prefix_holder = updated_freq, i + 1, string
