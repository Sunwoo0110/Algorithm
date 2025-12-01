def solution(sequence, k):
    n = len(sequence)
    
    answer = [n-1, 2*(n-1)]
    left, right = 0, 0
    
    total = 0
    
    for right in range(n):
        total += sequence[right]

        while total > k:
            total -= sequence[left]
            left += 1
        
        if total == k:
            if right-left < answer[1]-answer[0] or (right-left == answer[1]-answer[0] and left < answer[0]):
                answer[0], answer[1] = left, right
            
        
    
    
    return answer