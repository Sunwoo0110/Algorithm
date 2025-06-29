def to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

def to_time_string(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def solution(play_time, adv_time, logs):
    play_sec = to_seconds(play_time)
    adv_sec = to_seconds(adv_time)

    time_line = [0] * (play_sec + 2) ## 초당 시청자 수

    for log in logs:
        start, end = log.split('-')
        start_sec = to_seconds(start)
        end_sec = to_seconds(end)
        time_line[start_sec] += 1
        time_line[end_sec] -= 1

    # 누적합: 초당 시청자 수
    for i in range(1, play_sec + 1):
        time_line[i] += time_line[i - 1]

    # 누적합: 0~i초까지의 누적 재생시간
    for i in range(1, play_sec + 1):
        time_line[i] += time_line[i - 1]

    max_time = time_line[adv_sec - 1]
    max_start = 0

    for end in range(adv_sec, play_sec):
        current = time_line[end] - time_line[end - adv_sec] ## 재생시간
        if current > max_time:
            max_time = current
            max_start = end - adv_sec + 1

    return to_time_string(max_start)

