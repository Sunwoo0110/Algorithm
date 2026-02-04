import sys

def main():
    input = sys.stdin.readline
    
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    answer = n+1
    total = 0
    left = 0
    
    for right in range(n):
        total += arr[right]
        
        while left <= right and total >= s:
            answer = min(answer, right-left+1)
            total -= arr[left]
            left += 1
    
    if answer != n+1:
        print(answer)
    else:
        print(0)
            
if __name__ == "__main__":
    main()