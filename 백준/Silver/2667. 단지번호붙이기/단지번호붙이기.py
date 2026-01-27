import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    n = int(input())
    arr = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    
    def bfs(i, j):
        cnt = 1
        queue = deque()
        queue.append((i, j))
        visited[i][j] = True
        
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nx, ny = x+dx, y+dy
                
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == 1:
                    visited[nx][ny] = True
                    cnt += 1
                    queue.append((nx, ny))
        return cnt
    
    result = []          
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] == 1:
                cnt = bfs(i, j)
                result.append(cnt)
                
    result.sort()
    print(len(result))
    for r in result:
        print(r)
            
if __name__ == "__main__":
    main()
