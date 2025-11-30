def solution(n):
    answer = 0
    
    ## 같은 column / 대각선에 이미 퀸이 있는지 체크용
    cols = set()       ## 사용 중인 열
    diag1 = set()      ## r-c
    diag2 = set()      ## r+c

    def dfs(row):
        nonlocal answer

        # n개의 퀸을 모두 놓은 경우
        if row == n:
            answer += 1
            return
        
        for c in range(n):
            if c in cols or (row-c) in diag1 or (row+c) in diag2:
                continue
            
            cols.add(c)
            diag1.add(row-c)
            diag2.add(row+c)

            dfs(row+1)

            cols.remove(c)
            diag1.remove(row-c)
            diag2.remove(row+c)

    dfs(0)
    return answer
