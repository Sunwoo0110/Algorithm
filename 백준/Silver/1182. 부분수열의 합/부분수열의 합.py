import sys

def main():
    input = sys.stdin.readline
    
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    answer = 0
    
    def dfs(idx, total):
        nonlocal answer
        
        if idx == n:
            if total == s:
                answer += 1
            return
        
        dfs(idx+1, total+arr[idx])
        dfs(idx+1, total)
    
    dfs(0, 0)
    print(answer) if s != 0 else print(answer-1)
    
    
if __name__ == "__main__":
    main()
