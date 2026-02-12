import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    n, k = map(int, input().split())
    
    dist = [-1 for _ in range(100001)]
    dist[n] = 0
    
    prev = [-1 for _ in range(100001)]
    
    queue = deque()
    queue.append(n)
    
    while queue:
        cur_n = queue.popleft()
        
        if cur_n == k:
            print(dist[cur_n])
            break
        
        if cur_n-1 >= 0 and dist[cur_n-1] == -1:
            dist[cur_n-1] = dist[cur_n]+1
            queue.append(cur_n-1)
            prev[cur_n-1] = cur_n
            
        if cur_n+1 <= 100000 and dist[cur_n+1] == -1:
            dist[cur_n+1] = dist[cur_n]+1
            queue.append(cur_n+1)
            prev[cur_n+1] = cur_n
        
        if cur_n*2 <= 100000 and dist[cur_n*2] == -1:
            dist[cur_n*2] = dist[cur_n]+1
            queue.append(cur_n*2)
            prev[cur_n*2] = cur_n
    
    path = []
    cur = k
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    path = path[::-1]
    print(*path)
            
if __name__ == "__main__":
    main()