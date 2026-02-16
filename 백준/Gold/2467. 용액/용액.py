import sys

def main():
    input = sys.stdin.readline
    
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    left, right = 0, n-1
    gap = abs(arr[n-1]+arr[0])
    answer = [0, 0]
    
    while left < right:
        total = abs(arr[right]+arr[left])
        
        if total <= gap:
            answer = [arr[left], arr[right]]
            gap = total
        
        if abs(arr[left]+arr[right-1]) < abs(arr[left+1]+arr[right]):
            right -= 1
        else:
            left += 1
    
    print(*answer)
    
    
if __name__ == "__main__":
    main()
