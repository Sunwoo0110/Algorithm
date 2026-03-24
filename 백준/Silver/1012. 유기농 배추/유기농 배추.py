import sys
import heapq

def main():
    input = sys.stdin.readline
    
    T = int(input())
    
    def dfs(x, y):
        stack = [(x, y)]
        visited[x][y] = True
        
        while stack:
            cur_x, cur_y = stack.pop()
            
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx, ny = cur_x+dx, cur_y+dy
                
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                
                if not visited[nx][ny] and board[nx][ny] == 1:
                    stack.append((nx, ny))
                    visited[nx][ny] = True
    
    for _ in range(T):
        n, m, k = map(int, input().split())
        
        board = [[0 for _ in range(m)] for _ in range(n)]
        
        for _ in range(k):
            x, y = map(int, input().split())
            board[x][y] = 1
        
        answer = 0
        visited = [[False for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and board[i][j] == 1:
                    dfs(i, j)
                    answer += 1
        
        print(answer)
    
if __name__ == "__main__":
    main()