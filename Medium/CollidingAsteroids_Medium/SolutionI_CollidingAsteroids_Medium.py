# Algorithmic Beauty Bless You - O(n) time | O(n) space
def collidingAsteroids(asteroids):
    stack = []
    for aster in asteroids:
        if aster > 0:
            stack.append(aster)
            continue
        while stack and stack[-1] > 0:
            if stack[-1] > -aster:
                break
            popped = stack.pop()
            if popped == -aster:
                break
        else:
            stack.append(aster)
    return stack
