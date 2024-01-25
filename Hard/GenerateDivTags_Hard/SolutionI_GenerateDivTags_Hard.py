# Algorithmic Beauty Bless You - O((2n)!/(n!(n+1)!)) time | O((2n)!/(n!(n+1)!)) space
def generateDivTags(numberOfTags):
    generated, opening_tag, closing_tag = [], '<div>', '</div>'
    current, stack = [0, 0, ''], []
    while True:
        if current:
            stack.append(current)
            o_tag_cnt, c_tag_cnt, prefix = current
            if o_tag_cnt < numberOfTags:
                current = [o_tag_cnt + 1, c_tag_cnt, prefix + opening_tag]
            else:
                current = None
        elif stack:
            o_tag_cnt, c_tag_cnt, prefix = stack.pop()
            if c_tag_cnt < o_tag_cnt:
                c_tag_cnt += 1
                prefix += closing_tag
                if c_tag_cnt != numberOfTags:
                    current = [o_tag_cnt, c_tag_cnt, prefix]
                    continue
                generated.append(prefix)
            current = None
        else:
            break
    return generated
