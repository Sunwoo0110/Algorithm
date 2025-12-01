from collections import deque

def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    queue = deque()
    queue.append((0, 0, 1)) ## x, y, 이동 거리
    
    visited = set()
    visited.add((0, 0))
    
    while queue:
        x, y, l = queue.popleft()
        
        if x == n-1 and y == m-1:
            return l
         
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and maps[nx][ny] == 1:
                queue.append((nx, ny, l+1))
                visited.add((nx, ny))
    
    return answer