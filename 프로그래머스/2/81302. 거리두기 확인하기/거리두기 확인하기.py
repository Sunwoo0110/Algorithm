from collections import deque

def check(place): 
    for i in range(5):
        for j in range(5):
            if place[i][j] != 'P':
                continue
            
            ## (i,j)에서 BFS 시작
            queue = deque()
            queue.append((i, j, 0))
            visited = [[False]*5 for _ in range(5)]
            visited[i][j] = True
            
            while queue:
                x, y, dist = queue.popleft()
                
                ## 거리 2까지만 확인
                if dist >= 2:
                    continue
                
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x+dx, y+dy
                    if not (0 <= nx < 5 and 0 <= ny < 5):
                        continue
                    if visited[nx][ny]:
                        continue
                    if place[nx][ny] == 'X':  ## 파티션이면 더 안감
                        continue
                    
                    ## 빈 자리(O)이면 계속 탐색
                    if place[nx][ny] == 'O':
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist+1))
                    
                    ## 응시자(P)를 찾음 -> 거리두기 위반
                    if place[nx][ny] == 'P':
                        return 0
    return 1

def solution(places):
    answer = []
    
    for place in places:
        answer.append(check(place))
        
    return answer