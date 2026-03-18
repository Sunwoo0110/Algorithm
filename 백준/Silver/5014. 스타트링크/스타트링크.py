import sys
from collections import deque
import heapq

def main():
    input = sys.stdin.readline
    
    F, S, G, U, D = map(int, input().split())
    
    dist = [-1 for _ in range(F+1)]
    dist[S] = 0
    
    queue = deque()
    queue.append(S)

    while queue:
        node = queue.popleft()
        
        if node == G:
            print(dist[node])
            return
        
        if node+U <= F and (dist[node+U] == -1 or dist[node]+1 < dist[node+U]):
            dist[node+U] = dist[node]+1
            queue.append(node+U)
        
        if node-D > 0 and (dist[node-D] == -1 or dist[node]+1 < dist[node-D]):
            dist[node-D] = dist[node]+1
            queue.append(node-D)
        
    print("use the stairs")
    

if __name__ == "__main__":
    main()