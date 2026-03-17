import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    n, h = map(int, input().split())
    
    prefix = [0 for _ in range(h+1)]
    
    for i in range(n):
        height = int(input())
        if i%2 == 0:
            prefix[0] += 1
            prefix[height] -= 1
        else:
            prefix[h-height] += 1
            prefix[h] -= 1
    
    ## 누적합
    for i in range(h-1):
        prefix[i+1] += prefix[i]
    
    prefix.pop()
    min_broke = min(prefix)
    cnt = sum([1 for p in prefix if p == min_broke])
    
    print(f"{min_broke} {cnt}")
    
            

if __name__ == "__main__":
    main()