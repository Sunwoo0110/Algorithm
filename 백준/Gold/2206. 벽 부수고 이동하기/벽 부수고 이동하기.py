import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    board = []
    
    for _ in range(n):
        board.append(list(map(int, input().strip())))
    
    ## 0: 파괴 안한 경우, 1: 파괴한 경우
    visited = [[[False for _ in range(2)] for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = True
    
    queue = deque()
    queue.append((0, 0, 1, 0)) ## x, y, 길이, 벽 파괴 여부
    
    while queue:
        x, y, l, isBroken = queue.popleft()
        
        if x == n-1 and y == m-1:
            print(l)
            return

        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = x+dx, y+dy
            
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0:
                    if not visited[nx][ny][isBroken]:
                        visited[nx][ny][isBroken] = True
                        queue.append((nx, ny, l+1, isBroken))
                else:
                    if isBroken == 0 and not visited[nx][ny][1]:
                        visited[nx][ny][1] = True
                        queue.append((nx, ny, l+1, 1))
    
    print(-1)
    
if __name__ == "__main__":
    main()
