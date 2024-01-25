def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    schedules = []
    calendar1.append([dailyBounds1[1]])
    calendar2.append([dailyBounds2[1]])
    avail1 = anti_format_block([dailyBounds1[0], calendar1[0][0]])
    avail2 = anti_format_block([dailyBounds2[0], calendar2[0][0]])
    index1 = 0
    index2 = 0
    while True:
        max_left = max(avail1[0], avail2[0])
        min_right = min(avail1[1], avail2[1])
        if min_right - max_left >= meetingDuration:
            schedules.append(format_block([max_left, min_right]))
        move1 = avail1[1] <= avail2[1]
        move2 = avail2[1] <= avail1[1]
        if move1:
            index1 += 1
            if index1 == len(calendar1):
                break
            avail1 = anti_format_block([calendar1[index1 - 1][1], calendar1[index1][0]])
        if move2:
            index2 += 1
            if index2 == len(calendar2):
                break
            avail2 = anti_format_block([calendar2[index2 - 1][1], calendar2[index2][0]])
    return schedules


def anti_format_block(block):
    def anti_format_time(formatted_time):
        hour, minute = map(int, formatted_time.split(':'))
        return hour * 60 + minute

    return [anti_format_time(block[0]), anti_format_time(block[1])]


def format_block(block):
    def format_time(time_in_minutes):
        hour = time_in_minutes // 60
        minute = time_in_minutes % 60
        return f'{hour}:{minute:0>2d}'

    return [format_time(block[0]), format_time(block[1])]
