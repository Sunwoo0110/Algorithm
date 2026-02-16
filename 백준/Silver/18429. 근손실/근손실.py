import sys

def main():
    input = sys.stdin.readline
    
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    answer = 0
    visited = [False for _ in range(n)]
    
    def dfs(idx, total):
        nonlocal answer
        
        if idx == n:
            if total >= 500:
                answer += 1
            return

        for i in range(n):
            if not visited[i] and total+arr[i]-k >= 500:
                visited[i] = True
                dfs(idx+1, total+arr[i]-k)
                visited[i] = False
    
    dfs(0, 500)
    print(answer)
        
    
    
if __name__ == "__main__":
    main()
