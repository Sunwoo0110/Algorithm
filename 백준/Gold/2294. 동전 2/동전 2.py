import sys

def main():
    input = sys.stdin.readline
    
    n, k = map(int, input().split())
    arr = []
    
    for _ in range(n):
        arr.append(int(input()))
    
    INF = int(1e9)
    dp = [ INF for _ in range(k+1)]
    dp[0] = 0
    
    for a in arr:
        for j in range(a, k+1):
            dp[j] = min(dp[j], dp[j-a]+1)
    
    if dp[k] == INF:
        print(-1)
    else:
        print(dp[k])
    
if __name__ == "__main__":
    main()