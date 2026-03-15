import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    m, n, k = map(int, input().split())
    board = [[0 for _ in range(n)] for _ in range(m)]
    
    for _ in range(k):
        x1, y1, x2, y2 = map(int, input().split())
        
        for y in range(y1, y2):
            for x in range(x1, x2):
                board[y][x] = 1
    
    visited = [[False for _ in range(n)] for _ in range(m)]
    def dfs(x, y):
        
        stack = []
        stack.append((x, y))
        s = 0
        visited[x][y] = True
        
        while stack:
            cur_x, cur_y = stack.pop()
            s += 1
            
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = cur_x+dx, cur_y+dy
                
                if not ( 0 <= nx < m and 0 <= ny < n):
                    continue
                
                if not visited[nx][ny] and board[nx][ny] == 0:
                    stack.append((nx, ny))
                    visited[nx][ny] = True
        return s
    
    cnt = 0
    size = []
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and board[i][j] == 0:
                cnt += 1
                s = dfs(i, j)
                size.append(s)
    
    print(cnt)
    size.sort()
    print(*size)
        
        
    
    
if __name__ == "__main__":
    main()
    