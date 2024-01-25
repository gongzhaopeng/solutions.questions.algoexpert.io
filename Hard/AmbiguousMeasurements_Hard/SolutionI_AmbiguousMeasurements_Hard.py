# Algorithmic Beauty Bless You - O(low*high*n) time | O(low*high) space
def ambiguousMeasurements(measuringCups, low, high):
    dpt = {}
    current, stack, matched = [(low, high), 0], [], False
    while True:
        if current:
            low, high = interval = current[0]
            if high >= 0:
                if low <= 0:
                    matched, current = True, None
                    continue
            else:
                matched, current = False, None
                continue
            matched = dpt.get(interval)
            if matched is not None:
                current = None
                continue
            stack.append(current)
            current = [(low - measuringCups[0][0], high - measuringCups[0][1]), 0]
        elif stack:
            interval, p_visiting = stack[-1]
            p_visiting += 1
            if matched or p_visiting == len(measuringCups):
                dpt[interval] = matched
                stack.pop()
                current = None
                continue
            stack[-1][1] = p_visiting
            current = [(interval[0] - measuringCups[p_visiting][0], interval[1] - measuringCups[p_visiting][1]), 0]
        else:
            break
    return matched
