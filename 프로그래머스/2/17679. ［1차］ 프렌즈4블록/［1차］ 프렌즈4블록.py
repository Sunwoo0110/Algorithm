def solution(m, n, board):
    answer = 0
    changed = True
    
    board = [list(row) for row in board]
    
    while(changed):
        changed = False
        removed = [[False for _ in range(n)] for _ in range(m)]
        
        ## 2x2 배열 찾기
        for i in range(m-1):
            for j in range(n-1):
                curr = board[i][j]
                if curr != " " and curr == board[i+1][j] and curr == board[i][j+1] and curr == board[i+1][j+1]:
                    changed = True
                    removed[i][j] = removed[i+1][j] = removed[i][j+1] = removed[i+1][j+1] = True
        
        ## 값 삭제하고, 카운트
        for i in range(m):
            for j in range(n):
                if removed[i][j]:
                    board[i][j] = " "
                    answer += 1
                    
        
        ## 아래로 내리기
        for j in range(n):
            k = m-1
            for i in range(m-1, -1, -1):
                if board[i][j] != " ":
                    board[k][j] = board[i][j]
                    k -= 1
                    
            for i in range(k+1):
                board[i][j] = " "
    
    return answer