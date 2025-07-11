def solution(land):
    answer = 0

    for i in range(1, len(land)):
        for j in range(4):
            maxNum = 0
            for k in range(4):
                if j==k: continue
                maxNum = max(maxNum, land[i-1][k])
                
            land[i][j] += maxNum
    
    answer = max(land[len(land)-1])
    
    return answer