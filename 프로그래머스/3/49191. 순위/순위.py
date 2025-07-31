from collections import defaultdict, deque

def solution(n, results):
    answer = 0
    
    win_graph = defaultdict(list)
    lose_graph = defaultdict(list)
    
    for a, b in results:
        win_graph[a].append(b)
        lose_graph[b].append(a)
    
    for i in range(1, n+1):
        visited = [False for _ in range(n+1)]
        visited[0] = True
        visited[i] = True
        
        queue = deque()
        queue.append(i)
        
        while queue:
            curr = queue.popleft()
            visited[curr] = True
            
            for next in win_graph[curr]:
                if visited[next] == False:
                    queue.append(next)
        
        queue.append(i)
        
        while queue:
            curr = queue.popleft()
            visited[curr] = True
            
            for next in lose_graph[curr]:
                if visited[next] == False:
                    queue.append(next)
        
        is_certain = True
        for v in visited:
            if v == False:
                is_certain = False
                break
                
        if is_certain: answer += 1
        
        
    return answer