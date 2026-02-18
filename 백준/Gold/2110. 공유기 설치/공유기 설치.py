import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    n, c = map(int, input().split())
    arr = []
    
    for _ in range(n):
        arr.append(int(input()))
        
    arr.sort()
    left, right = 1, arr[-1]-arr[0]
    answer = 0
    
    while left <= right:
        mid = (left+right)//2 ## 인접한 두 공유기 사이 최대 거리
        
        cnt = 1
        prev = arr[0]
        for i in range(1, n):
            if arr[i]-prev >= mid:
                cnt += 1
                prev = arr[i]
        
        if cnt >= c:
            answer = max(answer, mid)
            left = mid+1
        else:
            right = mid-1
                
    print(answer)
        
    
if __name__ == "__main__":
    main()