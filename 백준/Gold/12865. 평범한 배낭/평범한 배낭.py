import sys

def main():
    input = sys.stdin.readline
    
    n, k = map(int, input().split())
    
    dp = [0 for _ in range(k+1)]
    
    for _ in range(n):
        w, v = map(int, input().split())
        
        for s in range(k, w-1, -1):
            if dp[s-w]+v > dp[s]:
                dp[s] = dp[s-w]+v
    
    print(dp[k])
    
if __name__ == "__main__":
    main()