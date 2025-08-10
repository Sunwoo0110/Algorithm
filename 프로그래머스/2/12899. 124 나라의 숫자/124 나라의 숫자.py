import math

def solution(n):
    answer = ''
    
    n = int(n)
    result = ''
    
    while n > 0:
        n -= 1
        if n%3 == 0:
            num = '1'
        elif n%3 == 1:
            num = '2'
        elif n%3 == 2:
            num = '4'
        else:
            pass
        result += num
        n //= 3
    
    answer = result[::-1]
        
    return answer