import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    n = int(input())
    
    answer = 0
    
    col = [False] * n
    diag1 = [False] * (2*n)
    diag2 = [False] * (2*n)
    
    def dfs(r):
        nonlocal answer 
        
        if r == n:
            answer += 1
            return
        
        for c in range(n):
            d1 = r+c
            d2 = r-c
            
            if not col[c] and not diag1[d1] and not diag2[d2]:
                col[c], diag1[d1], diag2[d2] = True, True, True
                dfs(r+1)
                col[c], diag1[d1], diag2[d2] = False, False, False
    
    dfs(0)
    print(answer)
            
if __name__ == "__main__":
    main()
