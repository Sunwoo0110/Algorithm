def solution(storey):
    answer = 0
    
    while storey > 0:
        curr = storey%10 ## 1의 자리
        next = (storey//10)%10 ## 10의 자리
        
        if curr < 5:
            answer += curr
            storey //= 10
        elif curr > 5: 
            answer += (10-curr)
            storey = (storey//10)+1
        else:
            if next < 5:
                answer += curr
                storey //= 10
            else:
                answer += (10-curr)
                storey = (storey//10)+1
    return answer