# Algorithmic Beauty Bless You - O(s2*m+s1*n^2) time | O(s2*m+n+s1) space
def stringsMadeUpOfStrings(strings, substrings):
    trie = Trie()
    for s in substrings:
        trie.insert(s)
    return [_ for _ in strings if is_made_up_of_strings(_, trie)]


def is_made_up_of_strings(string, trie):
    stack, current, blocked = [], [0, 0, trie.root], set()
    while True:
        if current:
            begin, p_visiting, trie_node = current
            p_visiting, trie_node = next_suffix(string, p_visiting, trie_node)
            if not p_visiting:
                blocked.add(begin)
                current = None
                continue
            if p_visiting == len(string):
                return True
            current[1], current[2] = p_visiting, trie_node
            if p_visiting not in blocked:
                stack.append(current)
                current = [p_visiting, p_visiting, trie.root]
        elif stack:
            current = stack.pop()
        else:
            break
    return False


def next_suffix(string, p_visiting, trie_node):
    for p_visiting in range(p_visiting, len(string)):
        trie_node = trie_node.get(string[p_visiting])
        if not trie_node:
            break
        if Trie.END_SYMBOL in trie_node:
            return p_visiting + 1, trie_node
    return None, None


class Trie:
    END_SYMBOL = -1

    def __init__(self):
        self.root = {}

    def insert(self, string):
        current = self.root
        for ch in string:
            current = current.setdefault(ch, {})
        current[Trie.END_SYMBOL] = True
