import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    arr = []
    
    for _ in range(n):
        arr.append(int(input()))
        
    left, right = 0, min(arr)*m
    answer = 0
    
    while left <= right:
        mid = (left+right)//2
        
        total = 0
        for a in arr:
            total += mid//a
        
        if total >= m:
            answer = mid
            right = mid-1
        else:
            left = mid+1
    
    print(answer)
    
if __name__ == "__main__":
    main()