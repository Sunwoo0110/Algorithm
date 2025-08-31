def solution(n,a,b):
    answer = 0
    num = n 
    
    while num > 1:
        answer += 1
        num //= 2
    
    while n > 0:
        half = n//2
        
        if (a <= half and b > half) or (a > half and b <= half):
            break
            
        answer -= 1
        n = half
        if a > half:
            a -= half
        if b > half:
            b -= half

    return answer