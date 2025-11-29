def solution(board, moves):
    answer = 0
    n = len(board[0])
    
    stack = []
    new_board = [[] for _ in range(n)]

    for row in board[::-1]:
        for i in range(n):
            if row[i] != 0:
                new_board[i].append(row[i])
        
    for move in moves:
        if new_board[move-1]:
            if stack and stack[-1] == new_board[move-1][-1]:
                stack.pop()
                answer += 2
            else:
                stack.append(new_board[move-1][-1])
            new_board[move-1].pop()
            
    return answer