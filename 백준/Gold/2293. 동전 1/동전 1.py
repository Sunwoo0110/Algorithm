import sys

def main():
    input = sys.stdin.readline
    
    n, k = map(int, input().split())
    arr = []
    dp = [0 for _ in range(k+1)]
    dp[0] = 1
    
    for _ in range(n):
        num = int(input())
        arr.append(num)
    
    for a in arr:
        for s in range(a, k+1):
            dp[s] += dp[s-a]
    
    print(dp[k])
    
if __name__ == "__main__":
    main()
