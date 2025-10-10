def solution(board, aloc, bloc):
    n, m = len(board), len(board[0])
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    memo = {}

    def in_range(x, y):
        return 0 <= x < n and 0 <= y < m

    def dfs(ax, ay, bx, by, turn, state):
        key = (ax, ay, bx, by, turn, state)
        
        if key in memo:
            return memo[key]

        grid = [list(row) for row in state]

        ## 현재 차례인 플레이어가 서 있는 칸이 사라졌으면 패배
        cur_x, cur_y = (ax, ay) if turn == 0 else (bx, by)
        
        if not grid[cur_x][cur_y]:
            memo[key] = (False, 0)
            return memo[key]

        can_move = False
        win_moves, lose_moves = [], []

        for dx, dy in dirs:
            nx, ny = cur_x + dx, cur_y + dy
            if not in_range(nx, ny) or not grid[nx][ny]:
                continue

            can_move = True
            
            ## 현재 칸 밟고 떠나며 발판 제거
            grid[cur_x][cur_y] = 0
            new_state = tuple(tuple(row) for row in grid)

            if turn == 0:  ## A 차례 -> B 차례로
                opp_win, moves = dfs(nx, ny, bx, by, 1, new_state)
            else:          ## B 차례 -> A 차례로
                opp_win, moves = dfs(ax, ay, nx, ny, 0, new_state)

            # 복구
            grid[cur_x][cur_y] = 1

            # 상대가 지면(opp_win=False) -> 나는 이김
            if not opp_win:
                win_moves.append(moves+1)
            else:
                lose_moves.append(moves+1)

        if not can_move:
            memo[key] = (False, 0)
            return memo[key]

        if win_moves:  ##  이길 수 있으면 최소 턴
            res = (True, min(win_moves))
        else:          ## 전부 지면 최대 턴
            res = (False, max(lose_moves))

        memo[key] = res
        return res

    start_state = tuple(tuple(row) for row in board)
    _, answer = dfs(aloc[0], aloc[1], bloc[0], bloc[1], 0, start_state)
    return answer
