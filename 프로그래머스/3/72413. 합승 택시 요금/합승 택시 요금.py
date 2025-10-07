import heapq
from collections import defaultdict

def solution(n, s, a, b, fares):
    answer = 100000*200
    
    distance = [[100000*200 for _ in range(n+1)] for _ in range(n+1)]
    
    graph = defaultdict(list)
    
    for i, j, fee in fares:
        graph[i].append((j, fee))
        graph[j].append((i, fee))
        
    for start in range(1, n+1):
        distance[start][start] = 0
        
        pq = []
        heapq.heappush(pq, (0, start))

        while pq:
            dis, node = heapq.heappop(pq)
            
            if dis > distance[start][node]:
                continue

            for nxt, fee in graph[node]:
                if distance[start][nxt] > dis+fee:
                    distance[start][nxt] = dis+fee
                    heapq.heappush(pq, (dis+fee, nxt))
    
    for end in range(1, n+1):
        answer = min(distance[s][end]+distance[end][a]+distance[end][b], answer)
    
    return answer