import sys

def main():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    path = []
    
    def dfs(cnt, cur_num):
        if cnt == m:
            print(*path)
            return
        
        for nxt in range(cur_num, n+1):
            path.append(nxt)
            dfs(cnt+1, nxt)
            path.pop()
        
    dfs(0, 1)
    
            
if __name__ == "__main__":
    main()