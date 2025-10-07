def solution(m, n, board):
    answer = 0
    
    blocks = []
    
    for b in board:
        blocks.append(list(b))
        
    while True:
        remove_set = find_all_remove(blocks, m, n)    
        
        if len(remove_set) == 0:
            break
        
        answer += len(remove_set)
        blocks = remove_blocks(blocks, m, n, remove_set)
    
    
    return answer

def find_remove(blocks, m, n, x, y):
    px = [0, 1, 1, 0]
    py = [1, 1, 0, 0]
    
    icon = blocks[x][y]
    
    result = []
    
    for dx, dy in zip(px, py):
        nx, ny = x+dx, y+dy
        
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            return []
        
        if nx >= 0 and nx < m and ny >= 0 and ny < n and blocks[nx][ny] != icon:
            return []
        
        result.append((nx, ny))
        
    return result
    

def find_all_remove(blocks, m, n):
    remove_set = set()
    
    ## 삭제할 블록들 저장
    for i in range(m):
        for j in range(n):
            if blocks[i][j] != "":
                remove_set.update(find_remove(blocks, m, n, i, j))
    
    return remove_set
    
def remove_blocks(blocks, m, n, remove_set):
    
    ## 블록 아래로 밀기
    new_block = [["" for _ in range(n)] for _ in range(m)]
    for j in range(n):
        x, y = m-1 ,j
        for i in range(m-1, -1, -1):
            if (i, j) not in remove_set:
                new_block[x][y] = blocks[i][j]
                x -= 1
    
    return new_block
    
        
    
    
    