def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    
    acc = [[0 for _ in range(m+1)] for _ in range(n+1)] ## 누적합

    for typ, r1, c1, r2, c2, degree in skill:
        if typ == 1:
            degree = -degree

        acc[r1][c1] += degree
        acc[r1][c2+1] -= degree
        acc[r2+1][c1] -= degree
        acc[r2+1][c2+1] += degree

    ## 행 누적합
    for i in range(n+1):
        for j in range(1, m+1):
            acc[i][j] += acc[i][j-1]

    ## 열 누적합
    for j in range(m+1):
        for i in range(1, n+1):
            acc[i][j] += acc[i-1][j]

    for i in range(n):
        for j in range(m):
            if board[i][j] + acc[i][j] > 0:
                answer += 1

    return answer
