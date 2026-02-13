import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    r, c = map(int, input().split())
    board = []
    
    for _ in range(r):
        board.append(list(input().strip()))
    
    fire_queue = deque()
    fire_time = [[-1 for _ in range(c)] for _ in range(r)]
    
    queue = deque()
    time = [[-1 for _ in range(c)] for _ in range(r)]
    
    for x in range(r):
        for y in range(c):
            if board[x][y] == "J":
                queue.append((x, y))
                board[x][y] = "."
                time[x][y] = 0
            
            if board[x][y] == "F":
                fire_queue.append((x, y))
                fire_time[x][y] = 0
    
    ## 불 확산
    while fire_queue:
        fx, fy = fire_queue.popleft()
        
        cur_t = fire_time[fx][fy]
        
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = fx+dx, fy+dy
                    
            if 0 <= nx < r and 0 <= ny < c and fire_time[nx][ny] == -1 and board[nx][ny] != "#":
                fire_queue.append((nx, ny))
                fire_time[nx][ny] = cur_t+1
    
    while queue:
        cur_r, cur_c = queue.popleft()
        
        if cur_r == 0 or cur_r == r-1 or cur_c == 0 or cur_c == c-1:
            print(time[cur_r][cur_c]+1)
            return
        
        ## 지훈 이동
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = cur_r+dx, cur_c+dy
            
            if 0 <= nx < r and 0 <= ny < c and time[nx][ny] == -1 and board[nx][ny] == "." and (fire_time[nx][ny] == -1 or fire_time[nx][ny] > time[cur_r][cur_c]+1):
                queue.append((nx, ny))
                time[nx][ny] = time[cur_r][cur_c]+1
                
    print("IMPOSSIBLE")
            
if __name__ == "__main__":
    main()
