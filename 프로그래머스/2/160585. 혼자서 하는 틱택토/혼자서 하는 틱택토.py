def solution(board):
    answer = 1
    o_arr = []
    x_arr = []
    
    end_list = [[[0,0], [0,1], [0,2]], [[1,0], [1,1], [1,2]], [[2,0], [2,1], [2,2]], [[0,0], [1,0], [2,0]], [[0,1], [1,1], [2,1]], [[0,2], [1,2], [2,2]],
[[0,0],[1,1],[2,2]], [[0,2], [1,1], [2,0]]]
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                o_arr.append([i, j])
            elif board[i][j] == 'X':
                x_arr.append([i, j])
                
    o_cnt, x_cnt = len(o_arr), len(x_arr)
    
    ## 표시 잘못한 경우
    if (x_cnt > o_cnt) or (o_cnt-x_cnt > 1):
        return 0
    
    ## 이미 끝난 경우
    o_end, x_end = False, False
    for end in end_list:
        if not o_end:
            for e in end:
                o_end = True
                if e not in o_arr:
                    o_end = False
                    break

        if not x_end:
            for e in end:
                x_end = True
                if e not in x_arr:
                    x_end = False
                    break
        
        
        if (o_end == True and x_cnt+1 != o_cnt) or (x_end == True and x_cnt != o_cnt) or (o_end == True and x_end == True):
            return 0
    
    
    return answer