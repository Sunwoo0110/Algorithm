import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline

    n, m = map(int, input().split())
    str_set = set()
    
    for _ in range(n):
        str_set.add(input())
    
    cnt = 0
    for _ in range(m):
        target = input()
        
        if target in str_set:
            cnt += 1

    print(cnt)
    

if __name__ == "__main__":
    main()
