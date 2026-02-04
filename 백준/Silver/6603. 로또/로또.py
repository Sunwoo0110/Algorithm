import sys

def main():
    input = sys.stdin.readline
    
    def dfs(idx, path):
        
        if len(path) == 6:
            print(*path)
            return
        
        if idx == k:
            return
        
        path.append(S[idx])
        dfs(idx+1, path)
        path.pop()
        dfs(idx+1, path)
    
    while True:
        tc = list(map(int, input().split()))
        
        if tc[0] == 0:
            return
        
        k, S = tc[0], tc[1:]
        
        dfs(0, [])
        print()
        
            
if __name__ == "__main__":
    main()
