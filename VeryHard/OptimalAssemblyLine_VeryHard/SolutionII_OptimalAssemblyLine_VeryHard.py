# Algorithmic Beauty Bless You - O(n*s^2) time | O(s) space
def optimalAssemblyLine(stepDurations, numStations):
    num_steps = len(stepDurations)
    pre_dpt = [0] * num_steps
    cur_dpt = pre_dpt.copy()
    pre_dpt[0] = stepDurations[0]
    stop_step = num_steps - numStations + 1
    for step in range(1, stop_step):
        pre_dpt[step] = pre_dpt[step - 1] + stepDurations[step]
    for station in range(1, numStations):
        stop_step += 1
        for step in range(station, stop_step):
            last_station_duration, min_longest = 0, float('inf')
            for begin in reversed(range(station, step + 1)):
                last_station_duration += stepDurations[begin]
                min_longest = min(min_longest, max(last_station_duration, pre_dpt[begin - 1]))
            cur_dpt[step] = min_longest
        pre_dpt, cur_dpt = cur_dpt, pre_dpt
    return pre_dpt[-1]
