from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    queue = deque()
    
    ## 캐시 크기 0
    if cacheSize == 0:
        return 5*len(cities)
    
    for city in cities:
        city = city.upper()
        ## cache miss
        if city not in queue:
            ## 캐치 꽉 찼을 때
            if len(queue) >= cacheSize:
                queue.popleft()
            queue.append(city)
            answer += 5
        
        ## cache hit
        else:
            queue.remove(city)
            queue.append(city)
            answer += 1
                  
    return answer