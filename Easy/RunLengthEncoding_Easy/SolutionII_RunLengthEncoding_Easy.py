# Algorithmic Beauty Bless You - O(n) time | O(n) space
def runLengthEncoding(string):
    cypher, count = [], 1
    for i in range(1, len(string)):
        if string[i] != string[i - 1] or count == 9:
            cypher.extend([str(count), string[i - 1]])
            count = 0
        count += 1
    cypher.extend([str(count), string[-1]])
    return ''.join(cypher)
