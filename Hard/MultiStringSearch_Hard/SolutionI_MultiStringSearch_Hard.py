# Algorithmic Beauty Bless You - O(ns+bs) time | O(ns) space
def multiStringSearch(bigString, smallStrings):
    contained, trie = [False] * len(smallStrings), Trie(smallStrings)
    for i in range(len(bigString)):
        current = trie.root
        for j in range(i, len(bigString)):
            current = current.get(bigString[j])
            if current is None:
                break
            p_word = current.get(Trie.END_SYMBOL)
            if p_word is not None:
                contained[p_word] = True
    return contained


class Trie:
    END_SYMBOL = '*'

    def __init__(self, words):
        self.root = {}
        for i, word in enumerate(words):
            self.add_word(word, i)

    def add_word(self, word, index):
        current = self.root
        for ch in word:
            current = current.setdefault(ch, {})
        current[Trie.END_SYMBOL] = index
