# Algorithmic Beauty Bless You - O(nm) time | O(m) space
def commonCharacters(strings):
    commons = set(strings[0])
    for i in range(1, len(strings)):
        updated_commons = set()
        for c in strings[i]:
            if c in commons:
                updated_commons.add(c)
        commons = updated_commons
    return list(commons)
