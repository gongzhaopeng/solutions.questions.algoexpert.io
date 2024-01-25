# Algorithmic Beauty Bless You - O(nm*8^s) time | O(nm + ws) space
def boggleBoard(board, words):
    trie, found_words = Trie(), set()
    visited = [[False for _ in _] for _ in board]
    for word in words:
        trie.add(word)
    for m in range(len(board)):
        for n in range(len(board[m])):
            dfs_rooted_at(board, m, n, trie, found_words, visited)
    return found_words


def dfs_rooted_at(board, r_root, c_root, trie, found_words, visited):
    current = [r_root, c_root, None, trie.root]
    stack = []
    while True:
        if current:
            r, c, _, trie_node = current
            if visited[r][c]:
                current = None
                continue
            letter = board[r][c]
            trie_node = trie_node.get(letter)
            if not trie_node:
                current = None
                continue
            matched_word = trie_node.get(Trie.END_SYMBOL)
            if matched_word:
                found_words.add(matched_word)
            neighbors = collect_neighbors(board, r, c)
            current[2:] = neighbors, trie_node
            visited[r][c] = True
            stack.append(current)
            if neighbors:
                r, c = neighbors.pop()
                current = [r, c, None, trie_node]
            else:
                current = None
        elif stack:
            r, c, neighbors, trie_node = stack[-1]
            if neighbors:
                r_neighbor, c_neighbor = neighbors.pop()
                current = [r_neighbor, c_neighbor, None, trie_node]
            else:
                stack.pop()
                visited[r][c] = False
                current = None
        else:
            break


def collect_neighbors(board, row, col):
    neighbors = []
    max_row, max_col = len(board) - 1, len(board[0]) - 1
    if row > 0:
        neighbors.append([row - 1, col])
        if col > 0:
            neighbors.append([row - 1, col - 1])
        if col < max_col:
            neighbors.append([row - 1, col + 1])
    if row < max_row:
        neighbors.append([row + 1, col])
        if col > 0:
            neighbors.append([row + 1, col - 1])
        if col < max_col:
            neighbors.append([row + 1, col + 1])
    if col > 0:
        neighbors.append([row, col - 1])
    if col < max_col:
        neighbors.append([row, col + 1])
    return neighbors


class Trie:
    END_SYMBOL = '*'

    def __init__(self):
        self.root = {}

    def add(self, word):
        cur = self.root
        for letter in word:
            cur = cur.setdefault(letter, {})
        cur[Trie.END_SYMBOL] = word
