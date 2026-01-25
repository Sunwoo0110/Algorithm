import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    cur_sum = sum(arr[:k])
    result = cur_sum
    
    if n == k:
        print(sum(arr))
        return
    
    for i in range(n-k):
        cur_sum = cur_sum - arr[i] + arr[i+k]
        result = max(result, cur_sum)
    print(result)
    
            
if __name__ == "__main__":
    main()
