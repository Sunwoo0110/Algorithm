import sys
import heapq

def main():
    input = sys.stdin.readline
    
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    left, right = 0, n-1
    gap = abs(arr[right]+arr[left])
    answer = [arr[left], arr[right]]
    
    while left < right:
        total = arr[left]+arr[right]
        
        if abs(total) < gap:
            gap = abs(total)
            answer = [arr[left], arr[right]]
        
        if total > 0:
            right -= 1
        else:
            left += 1
    print(*answer)
    
if __name__ == "__main__":
    main()
