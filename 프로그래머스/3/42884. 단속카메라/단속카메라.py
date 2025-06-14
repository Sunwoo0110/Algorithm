def solution(routes):
    answer = 0
    
    routes.sort(key=lambda x: x[1])
    last_cam = -30001
    
    for route in routes:
        s, e = route
        
        if s > last_cam:
            answer += 1
            last_cam = e
        
    return answer