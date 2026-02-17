import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    n, k = map(int, input().split())
    dist = [-1 for _ in range(100001)]
    dist[n] = 0
    
    queue = deque()
    queue.append(n)
    
    while queue:
        node = queue.popleft()
        
        if dist[k] != -1 and dist[node] > dist[k]:
            continue
        
        if node-1 >= 0 and (dist[node-1] == -1 or dist[node-1] > dist[node]+1):
            dist[node-1] = dist[node]+1
            queue.append(node-1)
        
        if node+1 <= 100000 and (dist[node+1] == -1 or dist[node+1] > dist[node]+1):
            dist[node+1] = dist[node]+1
            queue.append(node+1)
            
        if node*2 <= 100000 and (dist[node*2] == -1 or dist[node*2] > dist[node]):
            dist[node*2] = dist[node]
            queue.appendleft(node*2)
    
    print(dist[k])
    
if __name__ == "__main__":
    main()
