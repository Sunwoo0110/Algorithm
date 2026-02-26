import sys
import heapq

def main():
    input = sys.stdin.readline
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    answer = [arr[0], arr[1], arr[2]]
    
    gap = abs(arr[0] + arr[1] + arr[2])
    
    for i in range(n-2):
        a = arr[i]
        left, right = i+1, n-1
        
        while left < right:
            total = a+arr[left]+arr[right]
            
            if abs(total) < gap:
                answer = [a, arr[left], arr[right]]
                gap = abs(total)
            
            if total > 0:
                right -= 1
            else:
                left += 1
    
    print(*answer)
        
    
    
if __name__ == "__main__":
    main()
