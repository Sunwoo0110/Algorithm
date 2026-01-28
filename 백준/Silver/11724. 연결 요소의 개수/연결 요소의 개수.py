import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    
    graph = defaultdict(list)
    
    for _ in range(m):
        a, b = map(int, input().split())
        
        graph[a].append(b)
        graph[b].append(a)
        
    visited = [False for _ in range(n+1)]
    
    def dfs(node):
        stack = []
        stack.append(node)
        visited[node] = True
        
        while stack:
            cur_n = stack.pop()
            
            for nxt in graph[cur_n]:
                if not visited[nxt]:
                    stack.append(nxt)
                    visited[nxt] = True
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    
    print(cnt)
            
if __name__ == "__main__":
    main()
