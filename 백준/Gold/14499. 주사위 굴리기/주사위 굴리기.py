import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    n, m, x, y, k = map(int, input().split())
    
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
        
    ways = list(map(int, input().split()))
    dirs = [[0, 0], [0, 1], [0, -1], [-1, 0], [1, 0]]
    
    ## [위, 바닥, 북, 남, 동, 서]
    dice = [0]*6
    
    for way in ways:
        nx, ny = x+dirs[way][0], y+dirs[way][1]
        if not (0 <= nx < n and 0 <= ny < m): 
            continue
        x, y = nx, ny
                
        top, bottom, north, south, east, west = dice
        
        if way == 1:
            dice = [west, east, north, south, top, bottom]
        elif way == 2:
            dice = [east, west, north, south, bottom, top]
        elif way == 3:
            dice = [south, north, top, bottom, east, west]
        else:
            dice = [north, south, bottom, top, east, west]
        
        if board[x][y] == 0:
            board[x][y] = dice[1]
        else:
            dice[1] = board[x][y]
            board[x][y] = 0

        print(dice[0])
        
            
if __name__ == "__main__":
    main()