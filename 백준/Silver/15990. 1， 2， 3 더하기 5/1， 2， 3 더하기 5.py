import sys

def main():
    input = sys.stdin.readline
    
    MOD = 1000000009
    
    n = int(input())
    arr = []
    
    for _ in range(n):
        arr.append(int(input()))
    
    max_num = max(arr)
    
    ## dp[i][j]: 합이 i이고 마지막 숫자가 j 인 경우의 수
    dp = [[0 for _ in range(4)] for _ in range(max_num+1)]
    dp[1][1] = 1
    dp[2][2] = 1
    dp[3][1] = 1
    dp[3][2] = 1
    dp[3][3] = 1
        
    for i in range(4, max_num+1):
        dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % MOD
        dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % MOD
        dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % MOD

    for a in arr:
        print((dp[a][1]+dp[a][2]+dp[a][3]) % MOD)
    
if __name__ == "__main__":
    main()