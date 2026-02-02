import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    
    board = [list(map(int, input().split())) for _ in range(n)]
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    def dfs(i, j):
        cnt = 0
        stack = [(i, j)]
        visited[i][j] = True
        
        while stack:
            x, y = stack.pop()
            
            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nx, ny = x+dx, y+dy
                
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    cnt += 1
                    stack.append((nx, ny))
                    
        return cnt
    
    
    empty_idx = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                empty_idx.append((i, j))

    answer = 0
    l = len(empty_idx)
    for a in range(l):
        for b in range(a+1, l):
            for c in range(b+1, l):
                x1, y1 = empty_idx[a]
                x2, y2 = empty_idx[b]
                x3, y3 = empty_idx[c]
                
                board[x1][y1] = board[x2][y2] = board[x3][y3] = 1
                visited = [[False for _ in range(m)] for _ in range(n)]
                total = 0
                for i in range(n):
                    for j in range(m):
                        if board[i][j] == 2 and not visited[i][j]:
                            cnt = dfs(i, j)
                            total += cnt ## 감염된 구역
                
                safe = (l-3)-total
                answer = max(answer, safe)
                board[x1][y1] = board[x2][y2] = board[x3][y3] = 0
    
    print(answer)
        
        
            
if __name__ == "__main__":
    main()
