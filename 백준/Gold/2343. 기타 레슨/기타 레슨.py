import sys

def main():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    answer = sum(arr)
    
    left, right = max(arr), sum(arr)
    
    while left <= right:
        mid = (left+right)//2
        
        cnt, total = 1, 0
        for a in arr:
            if total+a > mid:
                cnt += 1
                total = a
            else:
                total += a
        
        if cnt <= m:
            answer = min(answer, mid)
            right = mid-1
        else:
            left = mid+1
        
    print(answer)
    
    
if __name__ == "__main__":
    main()
