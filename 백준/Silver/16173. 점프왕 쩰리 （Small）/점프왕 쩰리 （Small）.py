import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    n = int(input())
    board = []
    
    for _ in range(n):
        board.append(list(map(int, input().split())))
    
    queue = deque()
    queue.append((0, 0))
    
    visited = [[False for _ in range(n)]for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        x, y  = queue.popleft()
        
        if x == n-1 and y == n-1:
            print("HaruHaru")
            return
        
        jump = board[x][y]

        for nx, ny in ((x + jump, y), (x, y + jump)):
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
            
    print("Hing")
                
                    
    
if __name__ == "__main__":
    main()
