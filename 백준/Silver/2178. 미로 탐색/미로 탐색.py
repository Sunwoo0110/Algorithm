import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    
    arr = [list(map(int, input().strip())) for _ in range(n)]
    
    queue = deque()
    queue.append((0, 0, 1))
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    ## BFS
    while queue:
        x, y, cnt = queue.popleft()
        
        if x == n-1 and y == m-1:
            print(cnt)
            return cnt
        
        for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nx, ny = x+dx, y+dy
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
                queue.append((nx, ny, cnt+1))
                visited[nx][ny] = True
    
    

if __name__ == "__main__":
    main()
