import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    n, l, r = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    def bfs(i, j):
        result = []
        
        queue = deque()
        queue.append((i, j))
        visited[i][j] = True
        total = board[i][j]
        result.append((i, j))
        
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nx, ny = x+dx, y+dy
                
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and l <= abs(board[x][y]-board[nx][ny]) <= r:
                    visited[nx][ny] = True
                    result.append((nx,ny))
                    queue.append((nx, ny))
                    total += board[nx][ny]
        
        return result, total//len(result)
    
    cnt = 0        
    while True:
        visited = [[False for _ in range(n)] for _ in range(n)]
        isChange = False
        
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    result, popul = bfs(i, j)
                    
                    if len(result) > 1:
                        isChange = True
                    
                    for a, b in result:
                        board[a][b] = popul
        
        if not isChange:
            print(cnt)
            break
        
        cnt += 1

if __name__ == "__main__":
    main()