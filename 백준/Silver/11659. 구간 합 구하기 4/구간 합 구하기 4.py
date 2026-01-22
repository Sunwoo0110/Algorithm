import sys

def main():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    for i in range(n-1):
        arr[i+1] += arr[i]
    
    for _ in range(m):
        s, e = map(int, input().split())
        sum = arr[e-1]-arr[s-2] if s > 1 else arr[e-1]
        print(sum)
    

if __name__ == "__main__":
    main()