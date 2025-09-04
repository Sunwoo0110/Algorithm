from heapq import heappush, heappop

def solution(board):
    n = len(board)
    
    ## 방향: 0=위, 1=오른쪽, 2=아래, 3=왼쪽
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    cost = [[[10**9]*n for _ in range(n)] for _ in range(4)]
    
    heap = []
    
    ## 처음 시작할 때 오른쪽, 아래 넣기
    for d in (1, 2):
        nx, ny = dirs[d][0], dirs[d][1]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
            cost[d][nx][ny] = 100
            heappush(heap, (100, nx, ny, d))
    
    while heap:
        c, x, y, d = heappop(heap)
        
        if c > cost[d][x][y]:
            continue
        
        if x == n-1 and y == n-1:
            return c
        
        for nd, (dx, dy) in enumerate(dirs):
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                nc = c+(100 if nd == d else 600)
                if cost[nd][nx][ny] > nc:
                    cost[nd][nx][ny] = nc
                    heappush(heap, (nc, nx, ny, nd))
    
    answer = min(cost[d][n-1][n-1] for d in range(4))
    return answer
