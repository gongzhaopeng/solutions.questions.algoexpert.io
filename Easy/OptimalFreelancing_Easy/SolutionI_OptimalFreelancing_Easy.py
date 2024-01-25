import operator


# Algorithmic Beauty Bless You - O(nlogn) time | O(1) space
def optimalFreelancing(jobs):
    jobs.sort(key=operator.itemgetter('payment'), reverse=True)
    duration, count, profit = 7, 0, 0
    schedule = [False] * duration
    for job in jobs:
        for d in reversed(range(min(job['deadline'], duration))):
            if not schedule[d]:
                schedule[d], count, profit = True, count + 1, profit + job['payment']
                if count == duration:
                    return profit
                break
    return profit
