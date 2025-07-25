from collections import defaultdict, deque

def solution(n, edge):
    answer = 0
    
    graph = defaultdict(list)
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    queue = deque()
    queue.append(1)
    
    dist = [-1 for _ in range(n+1)]
    dist[1] = 0
    
    while queue:
        curr = queue.popleft()
        
        for next in graph[curr]:
            if dist[next] == -1:
                dist[next] = dist[curr]+1
                queue.append(next)
    
    m = max(dist)
    
    for d in dist:
        if m == d:
            answer += 1
        
    return answer