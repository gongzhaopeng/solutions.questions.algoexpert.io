# Algorithmic Beauty Bless You - O(n) time | O(n) space
def runLengthEncoding(string):
    cypher, id_ch, count = [], string[0], 0
    for ch in string:
        if ch != id_ch or count == 9:
            cypher.extend([str(count), id_ch])
            id_ch, count = ch, 1
        else:
            count += 1
    cypher.extend([str(count), id_ch])
    return ''.join(cypher)
