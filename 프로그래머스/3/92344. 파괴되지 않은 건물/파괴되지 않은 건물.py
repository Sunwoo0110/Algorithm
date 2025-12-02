def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    
    prefix = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for typ, r1, c1, r2, c2, degree in skill:
        if typ == 1:
            degree *= -1
            
        prefix[r1][c1] += degree
        prefix[r2+1][c2+1] += degree
        prefix[r1][c2+1] -= degree
        prefix[r2+1][c1] -= degree
    
    for i in range(n):
        for j in range(1, m):
            prefix[i][j] += prefix[i][j-1]
    
    for j in range(m):
        for i in range(1, n):
            prefix[i][j] += prefix[i-1][j]
            
    for i in range(n):
        for j in range(m):
            if board[i][j]+prefix[i][j] >= 1:
                answer += 1
    
    return answer