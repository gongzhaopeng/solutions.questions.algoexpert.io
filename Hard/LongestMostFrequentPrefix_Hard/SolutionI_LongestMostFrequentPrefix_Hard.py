# Algorithmic Beauty Bless You - O(n*m) time | O(n*m) space
def longestMostFrequentPrefix(strings):
    trie = Trie()
    for word in strings:
        trie.add_word(word)
    lmf_prefix = (0, 0, None)  # (frequency, prefix_len, represent_word)
    stack = []
    while True:
        if trie:
            stack.append(trie)
            trie = trie.children.popitem()[1] if trie.children else None
        elif stack:
            trie = stack[-1]
            if trie.children:
                trie = trie.children.popitem()[1]
                continue
            stack.pop()
            if trie.frequency > lmf_prefix[0] or (
                    trie.frequency == lmf_prefix[0] and len(stack) > lmf_prefix[1]):
                lmf_prefix = (trie.frequency, len(stack), trie.represent_word)
            trie = None
        else:
            break
    return lmf_prefix[-1][:lmf_prefix[1]]


class Trie:
    def __init__(self, represent_word=None):
        self.children = {}
        self.frequency = 0
        self.represent_word = represent_word

    def add_word(self, word):
        current = self
        for ch in word:
            current = current.children.setdefault(ch, Trie(word))
            current.frequency += 1
        current.represent_word = word
