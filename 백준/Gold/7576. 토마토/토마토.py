import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    m, n = map(int, input().split())
    
    board = [list(map(int, input().split())) for _ in range(n)]
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    total = n*m
    queue = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                queue.append((i, j, 0))
                visited[i][j] = True
            elif board[i][j] == -1:
                total -= 1
    
    visited_cnt = 0        
    
    while queue:
        x, y, cur_date = queue.popleft()
        visited_cnt += 1
        
        if visited_cnt == total:
            print(cur_date)
            return
        
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = x+dx, y+dy
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny, cur_date+1))
    print(-1)
    return
        
        
            
if __name__ == "__main__":
    main()
