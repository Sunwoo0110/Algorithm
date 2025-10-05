def solution(routes):
    answer = 0
    
    prev = -30001
    
    routes.sort(key=lambda x: x[1])
    for a, b in routes:
        if prev < a:
            answer += 1
            prev = b
    
    return answer