def solution(n, s):
    answer = [0 for _ in range(n)]
    
    if n > s:
        return [-1]
    
    target = s//n
    remain = s%n
    
    for i in range(n-1, -1, -1):
        if remain <= 0:
            answer[i] = target
        else:
            answer[i] = target+1
            remain -= 1
    return answer