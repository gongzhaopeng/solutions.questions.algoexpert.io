# Algorithmic Beauty Bless You - O(n) time | O(d) space
def getLowestCommonManager(topManager, reportOne, reportTwo):
    candi_lcm, current, stack = None, topManager, []
    while True:
        if current:
            if current is reportOne or current is reportTwo:
                if candi_lcm:
                    return candi_lcm
                candi_lcm = current
            stack.append([current, 0])
            current = current.directReports[0] if current.directReports else None
        elif stack:
            stack[-1][1] += 1
            ancient, visiting_pos = stack[-1]
            if visiting_pos < len(ancient.directReports):
                current = ancient.directReports[visiting_pos]
            else:
                stack.pop()
                if ancient is candi_lcm:
                    candi_lcm = stack[-1][0]
                current = None


# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
