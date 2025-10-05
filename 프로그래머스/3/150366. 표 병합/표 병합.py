def solution(commands):
    answer = []
    
    board = [["" for _ in range(51)] for _ in range(51)]
    idx_board = [[(i, j) for j in range(51)] for i in range(51)]
    
    for command in commands:
        c_arr = command.split(" ")
        com = c_arr[0]
        
        if com == "UPDATE":
            if len(c_arr) == 4:
                r, c, value = c_arr[1:]
                r, c = int(r), int(c)
                r, c = idx_board[r][c]
                
                for i in range(1, 51):
                    for j in range(1, 51):
                        if idx_board[i][j] == (r, c):
                            board[i][j] = value
                            break              

            else:
                value1, value2 = c_arr[1:]
                
                for i in range(1, 51):
                    for j in range(1, 51):
                        if board[i][j] == value1:
                            board[i][j] = value2
            
        elif com == "MERGE":
            r1, c1, r2, c2 = map(int, c_arr[1:])
            r1, c1 = idx_board[r1][c1]
            r2, c2 = idx_board[r2][c2]
            
            value = ""
            
            if r1 == r2 and c1 == c2:
                continue
                
            if board[r1][c1] != "":
                value = board[r1][c1]
            else:
                value = board[r2][c2]
            
            cell_r, cell_c = 0, 0
            if r1 < r2 or (r1 == r2 and c1 < c2):
                cell_r, cell_c = idx_board[r1][c1]
            else:
                cell_r, cell_c = idx_board[r2][c2]
            
            board[cell_r][cell_c] = value
            for i in range(1, 51):
                for j in range(1, 51):
                    if idx_board[i][j] == (r1, c1) or idx_board[i][j] == (r2, c2):
                        idx_board[i][j] = (cell_r, cell_c)
                        board[i][j] = value
            
        elif com == "UNMERGE":
            r, c = map(int, c_arr[1:])
            r2, c2 = idx_board[r][c]
            value = board[r2][c2]
            
            for i in range(1, 51):
                for j in range(1, 51):
                    if idx_board[i][j] == (r2, c2):
                        idx_board[i][j] = (i, j)
                        board[i][j] = ""
            
            board[r][c] = value
            
        else:
            r, c = map(int, c_arr[1:])
            r, c = idx_board[r][c]
            if board[r][c] == "":
                answer.append("EMPTY")
            else:
                 answer.append(board[r][c])
        
    
    return answer