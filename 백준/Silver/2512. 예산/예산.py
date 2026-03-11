import sys

def main():
    input = sys.stdin.readline
    
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    
    left, right = 1, max(arr)
    answer = 0
    budget = 0
    
    while left <= right:
        mid = (left+right)//2
        
        total = 0
        for a in arr:
            if a < mid:
                total += a
            else:
                total += mid
        
        if total <= m:
            left = mid+1
        else:
            right = mid-1
            
        if total <= m and total > budget:
            answer = mid
            budget = total
    
    print(answer)
    return answer
    
if __name__ == "__main__":
    main()
