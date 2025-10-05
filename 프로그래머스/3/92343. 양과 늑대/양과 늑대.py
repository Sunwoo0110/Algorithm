from collections import defaultdict

def solution(info, edges):
    answer = 0
    n = len(info)
    
    graph = defaultdict(list)
    
    for a, b in edges:
        graph[a].append(b)
        
    def dfs(node, sheep, wolf, available):
        nonlocal answer
        answer = max(answer, sheep)
        
        # 가능한 다음 이동 후보를 모두 돌기
        for nxt in list(available):
            new_available = available.copy()
            new_available.remove(nxt)
            new_available.update(graph[nxt])
            
            if info[nxt] == 0:
                dfs(nxt, sheep+1, wolf, new_available)
            else:
                if sheep > wolf+1:  # 늑대 수 제한
                    dfs(nxt, sheep, wolf+1, new_available)

    dfs(0, 1, 0, set(graph[0])) 
    
    return answer