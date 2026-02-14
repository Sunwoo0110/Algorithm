import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [arr[0]]
    
    for i in range(1, n):
        if arr[i] > dp[-1]:
            dp.append(arr[i])
        else:
            left, right = 0, len(dp)-1
            idx = len(dp)-1
            
            while left <= right:
                mid = (left+right)//2
                
                if dp[mid] >= arr[i]:
                    idx = mid
                    right = mid-1
                else:
                    left = mid+1
            
            dp[idx] = arr[i]
    
    print(len(dp))
    
if __name__ == "__main__":
    main()