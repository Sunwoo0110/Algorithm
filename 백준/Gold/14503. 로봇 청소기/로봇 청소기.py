import sys

def main():
    input = sys.stdin.readline

    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    
    board = [list(map(int, input().split())) for _ in range(n)]
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    cnt = 0
    
    while True:
        if board[r][c] == 0:
            ## 칸 청소
            board[r][c] = 2
            cnt += 1
        
        isAvailable = False
        for dx, dy in dirs:
            nx, ny = r+dx, c+dy
            
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                isAvailable = True
                d = (d+3)%4
                
                if board[r+dirs[d][0]][c+dirs[d][1]] == 0:
                    r = r+dirs[d][0]
                    c = c+dirs[d][1]
                break
        
        if not isAvailable:
            if board[r+dirs[(d+2)%4][0]][c+dirs[(d+2)%4][1]] == 1:
                break
            else:
                r = r+dirs[(d+2)%4][0]
                c = c+dirs[(d+2)%4][1]
                
    print(cnt)
    

if __name__ == "__main__":
    main()
