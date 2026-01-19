import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline

    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    
    left = 0
    current = 0
    cnt = 0

    for right in range(n):
        current += arr[right]
        
        while current > m and left <= right:
            current -= arr[left]
            left += 1

        if current == m:
            cnt += 1
            current -= arr[left]
            left += 1

    print(cnt)
    

if __name__ == "__main__":
    main()
