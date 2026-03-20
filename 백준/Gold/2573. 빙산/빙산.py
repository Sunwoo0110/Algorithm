import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    
    board = []
    
    for _ in range(n):
        board.append(list(map(int, input().split())))
    
    answer = 1
    
    def dfs(x, y):
        stack = [(x, y)]
        visited[x][y] = True
        
        while stack:
            cur_x, cur_y = stack.pop()
            
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = cur_x+dx, cur_y+dy
                
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                
                if board[nx][ny] > 0 and not visited[nx][ny]:
                    stack.append((nx, ny))
                    visited[nx][ny] = True
    
    while True:
        
        ## 높이 변화 기록
        decrease = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if board[i][j] > 0:
                    cnt = 0
                    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        nx, ny = i+dx, j+dy
                        
                        if not (0 <= nx < n and 0 <= ny < m):
                            continue
                        
                        if board[nx][ny] == 0:
                            cnt += 1
                    decrease[i][j] = cnt
        
        ## 높이 변화
        for i in range(n):
            for j in range(m):
                if board[i][j] > 0:
                    if decrease[i][j] >= board[i][j]:
                        board[i][j] = 0
                    else:
                        board[i][j] -= decrease[i][j]
        
        ## 덩어리 갯수 확인
        visited = [[False for _ in range(m)] for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] > 0 and not visited[i][j]:
                    dfs(i, j)
                    cnt += 1
        
        if cnt >= 2:
            print(answer)
            break
            
        if cnt == 0:
            print(0)
            break
        
        answer += 1

if __name__ == "__main__":
    main()