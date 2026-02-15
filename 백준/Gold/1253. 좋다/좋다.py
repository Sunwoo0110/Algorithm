import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    answer = 0
    
    for i in range(n):
        l, r = 0, n-1
        
        while l < r:
            if l == i:
                l += 1
                continue
            
            if r == i:
                r -= 1
                continue
            
            if arr[l]+arr[r] > arr[i]:
                r -= 1
            elif arr[l]+arr[r] < arr[i]:
                l += 1
            else:
                answer += 1
                break
    
    print(answer)
    
    
if __name__ == "__main__":
    main()
