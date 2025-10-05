def solution(cap, n, deliveries, pickups):
    answer = 0
    d_remain = 0  # 아직 못 배달한 박스 수
    p_remain = 0  # 아직 못 수거한 박스 수

    # 뒤에서부터 확인
    for i in range(n-1, -1, -1):
        d_remain += deliveries[i]
        p_remain += pickups[i]

        # 아직 처리할 게 없으면 패스
        if d_remain == 0 and p_remain == 0:
            continue

        # 현재 남은 배달/수거 중 더 큰 값을 기준으로 몇 번 왔다 갔다 해야 하는지 결정
        while d_remain > 0 or p_remain > 0:
            d_remain -= cap
            p_remain -= cap
            answer += (i+1)*2  # 왕복 거리

    return answer
