from collections import defaultdict

def solution(tickets):
    answer = []
    
    graph = defaultdict(list)
    
    ## 정렬
    tickets.sort(reverse=True)
    
    ## 그래프 생성
    for s, e in tickets:
        graph[s].append(e)
        
    ## DFS
    path = []
    stack = ["ICN"]
    
    while stack:
        cur = stack[-1]
        
        if graph[cur]:
            stack.append(graph[cur].pop())
        else:
            path.append(stack.pop())
    
    answer = path[::-1]
    return answer