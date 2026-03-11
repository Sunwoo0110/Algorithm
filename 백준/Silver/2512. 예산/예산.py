import sys

def main():
    input = sys.stdin.readline
    
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    
    left, right = 1, max(arr)
    answer = 0
    
    while left <= right:
        mid = (left+right)//2
        
        total = 0
        for a in arr:
            if a < mid:
                total += a
            else:
                total += mid
        
        if total <= m:
            answer = mid
            left = mid + 1
        else:
            right = mid-1
                
    print(answer)
    
if __name__ == "__main__":
    main()