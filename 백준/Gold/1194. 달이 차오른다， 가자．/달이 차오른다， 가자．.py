import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    board = []
    
    for _ in range(n):
        board.append(list(input().strip()))
    
    visited = [[[False]*64 for _ in range(m)] for _ in range(n)]
    
    sx, sy = 0, 0
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == "0":
                sx, sy = i, j
                board[i][j] = "."
                break
    
    visited[sx][sy][0] = True
    
    queue = deque()
    queue.append((sx, sy, 0, 0))
    
    while queue:
        x, y, key_mask, dist = queue.popleft()
        
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = x+dx, y+dy
            
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == "#":
                    continue
                
                if board[nx][ny] == "1":
                    print(dist+1)
                    return
                
                if board[nx][ny] == "." and not visited[nx][ny][key_mask]:
                    visited[nx][ny][key_mask] = True
                    queue.append((nx, ny, key_mask, dist+1))
                
                if 'a' <= board[nx][ny] <= 'f':
                    nmask = key_mask | (1 << (ord(board[nx][ny])-ord('a')))
                    
                    if not visited[nx][ny][nmask]:
                        visited[nx][ny][nmask] = True
                        queue.append((nx, ny, nmask, dist+1))
                
                if 'A' <= board[nx][ny] <= 'F' and key_mask & (1 << (ord(board[nx][ny])-ord('A'))): 
                    if not visited[nx][ny][key_mask]:
                        visited[nx][ny][key_mask] = True
                        queue.append((nx, ny, key_mask, dist+1))
                        
    print(-1)  
    
if __name__ == "__main__":
    main()
