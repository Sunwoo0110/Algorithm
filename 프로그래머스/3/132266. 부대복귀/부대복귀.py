from collections import defaultdict, deque

def solution(n, roads, sources, destination):
    answer = []
    
    graph = defaultdict(list)
    
    for a, b in roads:
        graph[a].append(b);
        graph[b].append(a);
        
    dist = [-1 for _ in range(n+1)]
    dist[destination] = 0
    
    queue = deque()
    queue.append(destination)
    
    while queue:
        curr = queue.popleft()
        
        for next in graph[curr]:
            if dist[next] == -1:
                dist[next] = dist[curr]+1
                queue.append(next)
    
    for s in sources:
        answer.append(dist[s])
        
    return answer