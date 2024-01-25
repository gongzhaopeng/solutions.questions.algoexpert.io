# Algorithmic Beauty Bless You - O(nlogn) time | O(1) space
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort(reverse=fastest)
    blueShirtSpeeds.sort()
    return sum(map(max, zip(redShirtSpeeds, blueShirtSpeeds)))
