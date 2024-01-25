# Algorithmic Beauty Bless You - O(n) time | O(n) space
def sunsetViews(buildings, direction):
    buildings = zip(reversed(range(len(buildings))), reversed(buildings)) if direction == 'EAST' else enumerate(
        buildings)
    highest, reachable = 0, []
    for i, b in buildings:
        if b > highest:
            reachable.append(i)
            highest = b
    if direction == 'EAST':
        reachable.reverse()
    return reachable
