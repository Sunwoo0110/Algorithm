import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    
    for _ in range(m):
        s, e = map(int, input().split())
        
        start, end = n, -1
        
        left, right = 0, n-1
        
        while left <= right:
            mid = (left+right)//2
            
            if arr[mid] < s:
                left = mid+1
            else:
                start = min(mid, start)
                right = mid-1
        
        left, right = 0, n-1
        
        while left <= right:
            mid = (left+right)//2
            
            if arr[mid] > e:
                right = mid-1
            else:
                end = max(mid, end)
                left = mid+1
                
        if start > end:
            print(0)
        else:
            print(end-start+1)
    
                
                    
    
if __name__ == "__main__":
    main()