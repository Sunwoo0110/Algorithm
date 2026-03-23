import sys
from collections import defaultdict, deque

def main():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    
    graph = defaultdict(list)
    
    for _ in range(m):
        a, b = map(int, input().split())
        
        graph[a].append(b)
        graph[b].append(a)
    
    
    bacon = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        ## BFS
        for j in range(i+1, n+1):
            queue = deque()
            visited = [False for _ in range(n+1)]
            
            queue.append((i, 0))
            visited[i] = True
            
            while queue:
                node, cnt = queue.popleft()
                
                if node == j:
                    bacon[i][j] = cnt
                    bacon[j][i] = cnt
                    break
                    
                for nxt in graph[node]:
                    if not visited[nxt]:
                        queue.append((nxt, cnt+1))
                        visited[nxt] = True
    
    answer, min_bacon = 1, sum(bacon[1])
    for i in range(2, n+1):
        if sum(bacon[i]) < min_bacon:
            answer = i
            min_bacon = sum(bacon[i])
    
    print(answer)
        
        
    
if __name__ == "__main__":
    main()