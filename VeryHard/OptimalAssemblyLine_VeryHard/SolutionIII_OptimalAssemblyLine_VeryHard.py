# Algorithmic Beauty Bless You - O(s*log(sum(durs))) time | O(1) space
def optimalAssemblyLine(stepDurations, numStations):
    min_longest, max_longest = max(stepDurations), sum(stepDurations)
    while min_longest < max_longest:
        cur_longest = (min_longest + max_longest) // 2
        cur_station_dur, station_count, i = 0, 1, 0
        while i < (len(stepDurations)):
            if cur_station_dur + stepDurations[i] > cur_longest:
                station_count += 1
                if station_count > numStations:
                    break
                cur_station_dur = 0
            else:
                cur_station_dur, i = cur_station_dur + stepDurations[i], i + 1
        else:
            max_longest = cur_longest
            continue
        min_longest = cur_longest + 1
    return max_longest
