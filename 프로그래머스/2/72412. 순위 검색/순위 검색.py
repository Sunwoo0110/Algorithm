def solution(info, query):
    answer = []
    
    # 매핑
    L_MAP = {'cpp':0, 'java':1, 'python':2}
    P_MAP = {'backend':0, 'frontend':1}
    C_MAP = {'junior':0, 'senior':1}
    F_MAP = {'chicken':0, 'pizza':1}

    MAX_SCORE = 100000
    
    counts = [[[[[0]*(MAX_SCORE+1) for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(3)]


    ## info 전처리: 24조합만 점수 카운팅
    for row in info:
        l, p, c, f, s = row.split()
        s = int(s)
        counts[L_MAP[l]][P_MAP[p]][C_MAP[c]][F_MAP[f]][s] += 1

    ## 누적합: arr[x] = 점수가 x 이상인 인원 수
    for li in range(3):
        for pi in range(2):
            for ci in range(2):
                for fi in range(2):
                    arr = counts[li][pi][ci][fi] ## 0~100,000
                    running = 0
                    for sc in range(MAX_SCORE, -1, -1):
                        running += arr[sc]
                        arr[sc] = running

    ## 쿼리 처리: 각 차원별 후보 인덱스 만들고 해당 셀들의 arr[score] 합산
    for q in query:
        q = q.replace("and ", "").split()
        lq, pq, cq, fq, X = q[0], q[1], q[2], q[3], int(q[4])

        Ls = range(3) if lq == '-' else [L_MAP[lq]]
        Ps = range(2) if pq == '-' else [P_MAP[pq]]
        Cs = range(2) if cq == '-' else [C_MAP[cq]]
        Fs = range(2) if fq == '-' else [F_MAP[fq]]

        total = 0
        for li in Ls:
            for pi in Ps:
                for ci in Cs:
                    for fi in Fs:
                        total += counts[li][pi][ci][fi][X]
        answer.append(total)
    return answer
