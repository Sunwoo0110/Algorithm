import sys

def main():
    input = sys.stdin.readline
    
    n = int(input())
    t = [0]*(n+1)
    p = [0]*(n+1)

    for i in range(n):
        t[i], p[i] = map(int, input().split())

    dp = [0]*(n+1) ## i일부터 시작할 때 최대 수익

    for i in range(n-1, -1, -1):
        if i+t[i] <= n:
            dp[i] = max(dp[i+1], p[i]+dp[i+t[i]])
        else:
            dp[i] = dp[i+1]

    print(dp[0])
    
    
if __name__ == "__main__":
    main()