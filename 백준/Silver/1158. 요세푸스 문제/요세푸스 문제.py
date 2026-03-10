import sys

def main():
    input = sys.stdin.readline
    
    n, k = map(int, input().split())
    arr = [i for i in range(1, n+1)]
    
    idx = 0
    result = []
    
    while arr:
        idx = (idx+k-1) % len(arr)
        result.append(arr.pop(idx))
    
    print("<" + ", ".join(map(str, result)) + ">")

if __name__ == "__main__":
    main()