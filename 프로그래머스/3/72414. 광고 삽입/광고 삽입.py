def solution(play_time, adv_time, logs):
    answer = ''
    
    ## 초로 변환
    h, m, s = map(int, play_time.split(":"))
    sec_play_time = h*3600 + m*60 + s
    
    h, m, s = map(int, adv_time.split(":"))
    sec_adv_time = h*3600 + m*60 + s
    
    viewer = [0 for _ in range(sec_play_time+2)]
    
    # 로그 처리 (시작 +1, 끝 -1)
    for log in logs:
        start, end = log.split("-")
        h, m, s = map(int, start.split(":"))
        sec_start = h*3600 + m*60 + s
        h, m, s = map(int, end.split(":"))
        sec_end = h*3600 + m*60 + s
        
        viewer[sec_start] += 1
        viewer[sec_end] -= 1

    # 1차 누적합 -> 초별 시청자 수
    for i in range(1, sec_play_time+1):
        viewer[i] += viewer[i-1]

    # 2차 누적합 -> 0~t까지 누적 시청시간
    for i in range(1, sec_play_time+1):
        viewer[i] += viewer[i-1]
        
    # 광고 구간 내 최대 시청시간 찾기
    max_pt = viewer[sec_adv_time-1]
    max_start = 0

    for end_time in range(sec_adv_time, sec_play_time):
        total_watch = viewer[end_time]-viewer[end_time-sec_adv_time]
        if total_watch > max_pt:
            max_pt = total_watch
            max_start = end_time-sec_adv_time+1

    # 초 -> 시:분:초 변환
    h = max_start // 3600
    m = (max_start % 3600) // 60
    s = (max_start % 60)
    
    h = str(h) if h >= 10 else "0" + str(h)
    m = str(m) if m >= 10 else "0" + str(m)
    s = str(s) if s >= 10 else "0" + str(s)
    
    answer = f"{h}:{m}:{s}"
    return answer
