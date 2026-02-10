import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    k, n = map(int, input().split())
    arr = []
    
    for _ in range(k):
        arr.append(int(input()))
    
    left, right = 1, max(arr)
    answer = 0
    
    while left <= right:
        mid = (left+right)//2
        
        cnt = 0
        for a in arr:
            cnt += a//mid
        
        if cnt >= n:
            answer = max(answer, mid)
            left = mid+1
        else:
            right = mid-1
    
    print(answer)
            
if __name__ == "__main__":
    main()
