import sys
from collections import defaultdict

def main():
    
    n = int(input())
    m = int(input())
    
    graph = defaultdict(list)
    
    for _ in range(m):
        a, b = map(int, input().split())
        
        graph[a].append(b)
        graph[b].append(a)
        
    stack = []
    answer = 0
    stack.append(1)
    visited = [False for _ in range(n+1)]
    visited[1] = True
    
    while stack:
        node = stack.pop()
        
        for nxt in graph[node]:
            if not visited[nxt]:
                stack.append(nxt)
                visited[nxt] = True
                answer += 1
    
    print(answer)
    
    
if __name__ == "__main__":
    main()