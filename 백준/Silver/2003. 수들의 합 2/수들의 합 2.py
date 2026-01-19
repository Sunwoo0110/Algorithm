import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline

    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    
    left, right = 0, 0
    total = 0
    
    while right < n:
        
        if total+arr[right] == m:
            cnt += 1
            total -= arr[left]
            left += 1
        elif total+arr[right] < m:
            total += arr[right]
            right += 1
        else:
            total -= arr[left]
            left += 1
    print(cnt)
    

if __name__ == "__main__":
    main()
