# Algorithmic Beauty Bless You - O(n^2) time | O(n) space
def rectangleMania(coords):
    count = 0
    registry = {tuple(coord) for coord in coords}
    for i in range(0, len(coords) - 1):
        for j in range(i + 1, len(coords)):
            pt1, pt2 = coords[i], coords[j]
            if pt1[0] > pt2[0]:
                pt1, pt2 = pt2, pt1
            if pt1[0] == pt2[0] or pt1[1] >= pt2[1]:
                continue
            if (pt1[0], pt2[1]) in registry and (pt2[0], pt1[1]) in registry:
                count += 1
    return count
