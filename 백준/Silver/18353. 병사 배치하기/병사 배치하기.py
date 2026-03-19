import sys
from collections import deque
import heapq

def main():
    input = sys.stdin.readline
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [1 for _ in range(n)] ## dp[i] = i까지 가장 긴 감소하는 길이
    
    for i in range(n):
        for j in range(i):
            if arr[j] > arr[i]:
                dp[i] = max(dp[i], dp[j]+1)
    
    print(n-max(dp))
    

if __name__ == "__main__":
    main()