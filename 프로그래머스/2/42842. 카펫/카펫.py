def solution(brown, yellow):
    answer = []
    
    b_sum = (brown-4) // 2
    
    for num in range(b_sum-1, b_sum//2-1, -1):
        if yellow == num*(b_sum-num):
            answer = [num+2, b_sum-num+2]
            break
    
    return answer