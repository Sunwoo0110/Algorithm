def solution(n, times):    
    left, right = 1, max(times) * n
    answer = right
    
    while left <= right:
        mid = (left+right) // 2
        
        ## mid 시간 동안 처리 가능한 사람 수
        people = 0
        for t in times:
            people += mid // t
            
            if people >= n:
                break

        if people >= n:
            ## mid 시간으로도 n명을 다 처리 가능
            answer = mid
            right = mid-1
        else:
            ## mid 시간으로 부족
            left = mid+1
    
    return answer