# Algorithmic Beauty Bless You - O(n^2) time | O(n^2) space
def stableInternships(interns, teams):
    if not interns:
        return []
    matched, p_unchecked = [-1] * len(interns), 0
    rev_matched = matched.copy()
    team_prefers = [_.copy() for _ in teams]
    for team in range(len(teams)):
        for rank in range(len(interns)):
            team_prefers[team][teams[team][rank]] = rank
    intern, p_check = p_unchecked, 0
    while True:
        team = interns[intern][p_check]
        if rev_matched[team] < 0:
            matched[intern], rev_matched[team] = p_check, team_prefers[team][intern],
            p_unchecked += 1
            if p_unchecked >= len(interns):
                break
            intern, p_check = p_unchecked, 0
        elif team_prefers[team][intern] < rev_matched[team]:
            fail_intern = teams[team][rev_matched[team]]
            matched[intern], rev_matched[team] = p_check, team_prefers[team][intern]
            intern, p_check = fail_intern, matched[fail_intern] + 1
        else:
            p_check += 1
    return [[intern, interns[intern][p_team]] for intern, p_team in enumerate(matched)]
