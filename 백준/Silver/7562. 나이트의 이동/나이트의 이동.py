import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    T = int(input())
    
    for _ in range(T):  
        n = int(input())
        cur_x, cur_y = map(int, input().split())
        tar_x, tar_y = map(int, input().split())
        
        dist = [[-1 for _ in range(n)] for _ in range(n)]
        dist[cur_x][cur_y] = 0
        
        queue = deque()
        queue.append((cur_x, cur_y))
        
        while queue:
            x, y = queue.popleft()
            
            if x == tar_x and y == tar_y:
                print(dist[x][y])
                break
            
            for dx, dy in [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2]]:
                nx, ny = x+dx, y+dy
                
                if 0 <= nx < n and 0 <= ny < n:
                    if dist[nx][ny] == -1 or dist[x][y]+1 < dist[nx][ny]:
                        dist[nx][ny] =  dist[x][y]+1
                        queue.append((nx, ny))
            
    
if __name__ == "__main__":
    main()