# Algorithmic Beauty Bless You - O(nlog) time | O(1) space
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    taller, shorter = redShirtHeights, blueShirtHeights
    if taller[0] <= shorter[0]:
        taller, shorter = shorter, taller
    return next((i for i in range(len(taller)) if taller[i] <= shorter[i]), -1) < 0
