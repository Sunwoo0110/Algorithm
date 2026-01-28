import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    
    n_set = set()
    for _ in range(n):
        n_set.add(input().strip())
    
    result = []
    for _ in range(m):
        target = input().strip()
        if target in n_set:
            result.append(target)
    result.sort()
    
    print(len(result))
    
    for r in result:
        print(r)
            
if __name__ == "__main__":
    main()
