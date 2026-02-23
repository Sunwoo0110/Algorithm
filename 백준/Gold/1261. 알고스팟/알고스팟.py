import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    m, n = map(int, input().split())
    board = []
    
    for _ in range(n):
        board.append(list(map(int, list(input().strip()))))
    
    broken = [[-1 for _ in range(m)] for _ in range(n)]
    broken[0][0] = 0
    
    queue = deque()
    queue.append((0, 0))
    
    while queue:
        x, y = queue.popleft()
        
        if broken[n-1][m-1] != -1 and broken[n-1][m-1] < broken[x][y]:
            continue
        
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x+dx, y+dy
            
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0:
                    if broken[nx][ny] == -1 or broken[x][y] < broken[nx][ny]:
                        broken[nx][ny] = broken[x][y]
                        queue.append((nx, ny))
                else:
                    if broken[nx][ny] == -1 or broken[x][y]+1 < broken[nx][ny]:
                        broken[nx][ny] = broken[x][y]+1
                        queue.append((nx, ny))
    
    print(broken[n-1][m-1])
    
if __name__ == "__main__":
    main()
