import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    answer = 0
    
    for i in range(n):
        for j in range(i+1):
            answer += arr[j]
    
    print(answer)    
if __name__ == "__main__":
    main()