def solution(n):
    l = (n*(n+1))//2
    answer = [0 for _ in range(l)]
    
    map = [[0 for _ in range(n)] for _ in range(n)]
    
    dir = 0
    x = y = nx = ny = 0
    
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    
    for num in range(1, l+1):
        map[x][y] = num;
        
        nx = x+dx[dir]
        ny = y+dy[dir]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n or map[nx][ny] != 0:
            dir = (dir+1)%3
            nx = x+dx[dir]
            ny = y+dy[dir]
            
        x = nx
        y = ny
           
    idx = 0   
    for i in range(n):
        for j in range(i+1):
            answer[idx] = map[i][j]
            idx += 1
    
    return answer