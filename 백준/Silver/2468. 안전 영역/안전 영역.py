import sys

def main():
    input = sys.stdin.readline
    
    n = int(input())
    board = []
    min_h, max_h = 100, 1
    
    for _ in range(n):
        arr = list(map(int, input().split()))
        min_h, max_h = min(min_h, min(arr)), max(max_h, max(arr))
        board.append(arr)

    answer = 0
    
    def dfs(x, y):
        visited[x][y] = True
        
        stack = []
        stack.append((x, y))
        
        while stack:
            cur_x, cur_y = stack.pop()
            
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx, ny = cur_x+dx, cur_y+dy
                
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                
                if not visited[nx][ny] and board[nx][ny] > h:
                    stack.append((nx, ny))
                    visited[nx][ny] = True
    
    for h in range(min_h-1, max_h+1):
        visited = [[False for _ in range(n)] for _ in range(n)]
        cnt = 0
        
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and board[i][j] > h:
                    dfs(i, j)
                    cnt += 1
        
        answer = max(answer, cnt)
    
    print(answer)

if __name__ == "__main__":
    main()
