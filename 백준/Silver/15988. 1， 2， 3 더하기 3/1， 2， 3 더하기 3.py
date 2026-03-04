import sys

def main():
    input = sys.stdin.readline
    
    MOD = 1000000009
    
    T = int(input())
    nums = [int(input()) for _ in range(T)]
    max_num = max(nums)
    
    dp = [0 for _ in range(max_num+1)]
    dp[0] = 1
    
    if max_num >= 1:
        dp[1] = 1
    if max_num >= 2:
        dp[2] = 2
        
    for i in range(3, max_num+1):
        dp[i] = (dp[i-1]+dp[i-2]+dp[i-3])%MOD
    
    for num in nums:
        print(dp[num]%MOD)
        
if __name__ == "__main__":
    main()