import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    n, k = map(int, input().split())
    
    dp = [-1 for _ in range(200001)]
    
    queue = deque()
    queue.append(n)
    dp[n] = 0
    
    while queue:
        cur_p = queue.popleft()
        
        if cur_p == k:
            print(dp[cur_p])
            return
        
        nxt = cur_p+1
        if nxt <= 200000 and dp[nxt] == -1:
            dp[nxt] = dp[cur_p] + 1
            queue.append(nxt)

        nxt = cur_p-1
        if nxt >= 0 and dp[nxt] == -1:
            dp[nxt] = dp[cur_p] + 1
            queue.append(nxt)

        nxt = cur_p*2
        if nxt <= 200000 and dp[nxt] == -1:
            dp[nxt] = dp[cur_p] + 1
            queue.append(nxt)
            
if __name__ == "__main__":
    main()
