from collections import deque

def solution(maps):
    answer = -1
    
    path = [[0,1], [0,-1], [1,0], [-1,0]]
    visited = set()
    visited.add((0,0))
    
    n, m = len(maps), len(maps[0])
    
    queue = deque([(0,0,1)])
    
    while queue:
        x, y, distance = queue.popleft()
        
        if x == n-1 and y == m-1:
            return distance
        
        for dx, dy in path:
            nx, ny = x+dx, y+dy
            if nx >= 0 and nx < n and ny >= 0 and ny < m and (nx, ny) not in visited and maps[nx][ny] == 1:
                visited.add((nx, ny))
                queue.append((nx, ny, distance+1))
        
    return answer