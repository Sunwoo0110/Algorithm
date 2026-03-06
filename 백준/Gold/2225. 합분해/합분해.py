import sys

def main():
    input = sys.stdin.readline
    
    MOD = 1000000000
    
    n, k = map(int, input().split())
    
    ## dp[i][j] : j개 뽑아 합이 i가 되는 경우의 수
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][1] = 1
    
    for j in range(k+1):
        dp[0][j] = 1
    
    for i in range(1, n+1):
        for j in range(2, k+1):
            dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % MOD
    
    print(dp[n][k])
    
    
if __name__ == "__main__":
    main()