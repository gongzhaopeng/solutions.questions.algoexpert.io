def minRewards(scores):
    rewards = 0
    pre_dir = 1
    count = 0
    pre_peak = None
    for i in range(len(scores)):
        try:
            post_dir = 1 if scores[i + 1] > scores[i] else -1
        except IndexError:
            post_dir = -pre_dir
        count += 1
        rewards += count
        if pre_dir + post_dir == 0:
            if post_dir < 0:
                pre_peak = count
                count = 0
            else:
                if not count < pre_peak:
                    rewards += count + 1 - pre_peak
                count = 1
        pre_dir = post_dir
    return rewards
