import sys

def main():
    input = sys.stdin.readline
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    m = int(input())
    target = list(map(int, input().split()))
    
    arr.sort()
    
    for t in target:
        
        left, right = 0, n-1
        
        while left <= right:
            mid = (left+right) // 2
            
            if t == arr[mid]:
                print(1)
                break
            elif t < arr[mid]:
                right = mid-1
            else:
                left = mid+1
        
        if left > right:
            print(0)
    

if __name__ == "__main__":
    main()
