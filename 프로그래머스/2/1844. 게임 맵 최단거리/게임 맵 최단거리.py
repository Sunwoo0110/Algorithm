from collections import deque

def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])
    
    visited = [[False]*m for _ in range(n)]
    
    queue = deque()
    queue.append((0, 0, 1)) ## x, y, 현재 길이
    
    visited[0][0] = True
    
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    while queue:
        x, y, l = queue.popleft()
        
        if x == n-1 and y == m-1:
            return l
        
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if nx >= 0 and nx < n and ny >= 0 and ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, l+1))
        
    return answer