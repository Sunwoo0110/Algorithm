def solution(n, computers):
    answer = 0
    visited = set()
    
    def dfs(node):
        stack = [node]
        
        while stack:
            current = stack.pop()
            
            for i in range(n):
                if computers[current][i] == 1 and i not in visited:
                    visited.add(i)
                    stack.append(i)
                    
    for node in range(n):
        if node not in visited:
            dfs(node)
            visited.add(node)
            answer += 1
        
        
    return answer