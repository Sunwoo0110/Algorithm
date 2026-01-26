import sys

def main():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    left, right = 0, max(arr)
    answer = 0
    
    while left <= right:
        mid = (left+right) // 2
        
        wood = 0
        for a in arr:
            if a > mid:
                wood += a-mid

        if wood >= m:
            answer = mid          
            left = mid+1
        else:
            right = mid-1
    
    print(answer)
        
    
            
if __name__ == "__main__":
    main()
