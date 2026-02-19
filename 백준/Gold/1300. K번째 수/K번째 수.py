import sys

def main():
    input = sys.stdin.readline
    
    n = int(input())
    k = int(input())
    
    left, right = 1, n*n
    
    while left <= right:
        mid = (left+right)//2
        cnt = 0
        for i in range(1, n+1):
            cnt += min(n, mid//i)
        
        if cnt >= k:
            right = mid-1
        else:
            left = mid+1
    
    print(left)
    
if __name__ == "__main__":
    main()