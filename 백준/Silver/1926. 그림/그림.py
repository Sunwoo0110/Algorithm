import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    board = []
    
    for _ in range(n):
        board.append(list(map(int, input().split())))
    
    def dfs(x, y):
        cnt = 0
        
        stack = []
        stack.append((x, y))
        visited[x][y] = True
        
        while stack:
            cur_x, cur_y = stack.pop()
            cnt += 1
            
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = cur_x+dx, cur_y+dy
                
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                
                if not visited[nx][ny] and board[nx][ny] == 1:
                    stack.append((nx, ny))
                    visited[nx][ny] = True
        return cnt
    
    result = []
    paint_cnt = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and board[i][j] == 1:
                result.append(dfs(i, j))
                paint_cnt += 1
    
    print(paint_cnt)
    if result:
        print(max(result))
    else:
        print(0)
            

if __name__ == "__main__":
    main()