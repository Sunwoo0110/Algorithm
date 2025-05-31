def solution(A, B):
    answer = 0
    
    A.sort()
    B.sort()
    
    b_idx = 0
    
    ## 그리디
    for a in A:
        while b_idx < len(B) and B[b_idx] <= a:
            b_idx += 1
        
        if b_idx < len(B):
            answer += 1
            b_idx += 1

                
    return answer