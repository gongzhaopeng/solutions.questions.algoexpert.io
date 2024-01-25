def tournamentWinner(competitions, results):
    points = {}
    for comp, res in zip(competitions, results):
        points.setdefault(comp[0 if res else 1], [0])[0] += 3
    return max(points.items(), key=lambda item: item[1][0])[0]
