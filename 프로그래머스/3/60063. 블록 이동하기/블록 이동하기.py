from collections import deque

def solution(board):
    n = len(board)
    
    answer = n*n
    
    visited = set()
    visited.add((0, 0, 0, 1))
    
    queue = deque()
    queue.append((0, 0, 0, 1, 0))
    
    while queue:
        x1, y1, x2, y2, l = queue.popleft()
        
        if (x1, y1) == (n-1, n-1) or (x2, y2) == (n-1, n-1):
            answer = min(answer, l)
            continue
        
        ## 이동하기
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx1, ny1 = x1+dx, y1+dy
            nx2, ny2 = x2+dx, y2+dy
            
            if nx1 >=0 and nx1 < n and nx2 >=0 and nx2 < n and ny1 >=0 and ny1 < n and ny2 >=0 and ny2 < n and board[nx1][ny1] == 0 and board[nx2][ny2] == 0 and (nx1, ny1, nx2, ny2) not in visited:
                visited.add((nx1, ny1, nx2, ny2))
                queue.append((nx1, ny1, nx2, ny2, l+1))
        
        ## 회전하기
        
        if x1 == x2:
            ## 왼쪽 위로 회전
            if x2-1 >= 0 and x2-1 < n and y2-1 >= 0 and y2-1 < n and board[x2-1][y2] == 0 and board[x2-1][y2-1] == 0 and (x2-1, y2-1, x1, y1) not in visited:
                visited.add((x2-1, y2-1, x1, y1))
                queue.append((x2-1, y2-1, x1, y1, l+1))
            ## 오른쪽 위로 회전
            if x1-1 >= 0 and x1-1 < n and y1+1 >= 0 and y1+1 < n and board[x1-1][y1] == 0 and board[x1-1][y1+1] == 0 and (x1-1, y1+1, x2, y2) not in visited:
                visited.add((x1-1, y1+1, x2, y2))
                queue.append((x1-1, y1+1, x2, y2, l+1))
            ## 왼쪽 아래로 회전
            if x2+1 >= 0 and x2+1 < n and y2-1 >= 0 and y2-1 < n and board[x2+1][y2] == 0 and board[x2+1][y2-1] == 0 and (x1, y1, x2+1, y2-1) not in visited:
                visited.add((x1, y1, x2+1, y2-1))
                queue.append((x1, y1, x2+1, y2-1, l+1))
            ## 오른쪽 아래로 회전
            if x1+1 >= 0 and x1+1 < n and y1+1 >= 0 and y1+1 < n and board[x1+1][y1] == 0 and board[x1+1][y1+1] == 0 and (x2, y2, x1+1, y1+1) not in visited:
                visited.add((x2, y2, x1+1, y1+1))
                queue.append((x2, y2, x1+1, y1+1, l+1))
                
        if y1 == y2:
            ## 왼쪽 위로 회전
            if x2-1 >= 0 and x2-1 < n and y2-1 >= 0 and y2-1 < n and board[x2][y2-1] == 0 and board[x2-1][y2-1] == 0 and (x2-1, y2-1, x1, y1) not in visited:
                visited.add((x2-1, y2-1, x1, y1))
                queue.append((x2-1, y2-1, x1, y1, l+1))
            ## 오른쪽 위로 회전
            if x2-1 >= 0 and x2-1 < n and y2+1 >= 0 and y2+1 < n and board[x2][y2+1] == 0 and board[x2-1][y2+1] == 0 and (x1, y1, x2-1, y2+1) not in visited:
                visited.add((x1, y1, x2-1, y2+1))
                queue.append((x1, y1, x2-1, y2+1, l+1))
            ## 왼쪽 아래로 회전
            if x1+1 >= 0 and x1+1 < n and y1-1 >= 0 and y1-1 < n and board[x1][y1-1] == 0 and board[x1+1][y1-1] == 0 and (x1+1, y1-1, x2, y2) not in visited:
                visited.add((x1+1, y1-1, x2, y2))
                queue.append((x1+1, y1-1, x2, y2, l+1))
            ## 오른쪽 아래로 회전
            if x1+1 >= 0 and x1+1 < n and y1+1 >= 0 and y1+1 < n and board[x1][y1+1] == 0 and board[x1+1][y1+1] == 0 and (x2, y2, x1+1, y1+1) not in visited:
                visited.add((x2, y2, x1+1, y1+1))
                queue.append((x2, y2, x1+1, y1+1, l+1))
            
    
    return answer