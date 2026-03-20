import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    n = int(input())
    tx, ty = map(int, input().split())
    
    m = int(input())
    par_ch_graph = defaultdict(list)
    ch_par_graph = defaultdict(int)
    
    for _ in range(m):
        x, y = map(int, input().split())
        
        par_ch_graph[x].append(y)
        ch_par_graph[y] = x
    
    answer = 0
    
    stack = [(tx, 0)]
    par_visited = [False for _ in range(n+1)]
    ch_visited = [False for _ in range(n+1)]
    
    par_visited[tx] = True
    ch_visited[tx] = True
    
    while stack:
        cur_x, cnt = stack.pop()
        
        if cur_x == ty:
            print(cnt)
            return
        
        parent = ch_par_graph[cur_x]
        if parent > 0 and not par_visited[parent]:
            stack.append((parent, cnt+1))
            par_visited[parent] = True
        
        for nxt_ch in par_ch_graph[cur_x]:
            if not ch_visited[nxt_ch]:
                stack.append((nxt_ch, cnt+1))
                ch_visited[nxt_ch] = True
    
    print(-1)
        
        
    

if __name__ == "__main__":
    main()