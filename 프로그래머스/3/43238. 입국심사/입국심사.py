def solution(n, times):
    answer = 0
    
    left = 1
    right = min(times)*n
    
    while left < right:
        mid = (left+right) // 2 ## 최솟값 후보
        people = sum(mid//time for time in times) ## 심사 받을 수 있는 수
        
        if people >= n:
            right = mid
            
        else:
            left = mid+1
            
    answer = left
    return answer