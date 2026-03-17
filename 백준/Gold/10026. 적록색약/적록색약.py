import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    n = int(input())
    board = []
    
    for _ in range(n):
        board.append(list(input().strip()))
    
    def dfs(x, y, isRed):
        
        stack = []
        stack.append((x, y))
        
        color = board[x][y]
        visited[x][y] = True
        
        while stack:
            cur_x, cur_y = stack.pop()
            
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = cur_x+dx, cur_y+dy
                
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                
                if not visited[nx][ny]:
                    if board[nx][ny] == color or (isRed and color in ["R","G"] and board[nx][ny] in ["R","G"]):
                        stack.append((nx, ny))
                        visited[nx][ny] = True
        
    visited = [[False for _ in range(n)] for _ in range(n)]
    result = []
    
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                dfs(i, j, False)
                cnt += 1
    result.append(cnt)
    
    cnt = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                dfs(i, j, True)
                cnt += 1
    result.append(cnt)
    print(*result)
        
            

if __name__ == "__main__":
    main()