from collections import defaultdict

def solution(n, wires):
    answer = 100
    visited = set()
        
    def dfs(node, graph):
        stack = [node]
        
        while stack:
            current = stack.pop()
            
            for next_node in graph[current]:
                if next_node not in visited:
                    stack.append(next_node)
                    visited.add(next_node)
            
    for i in range(len(wires)):
        ## 새로운 그래프 생성
        graph = defaultdict(list)
        visited = set()
        visited.add(1)
        
        for j in range(len(wires)):
            if i != j:
                graph[wires[j][0]].append(wires[j][1])
                graph[wires[j][1]].append(wires[j][0])
                
        dfs(1, graph)
        gap = abs(n - 2 * len(visited))
        answer = min(answer, gap)
    
    return answer