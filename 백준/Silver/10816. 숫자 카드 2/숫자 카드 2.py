import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline

    n = input().strip().split()
    A = list(map(int, input().split()))
    m = input().strip().split()
    B = list(map(int, input().split()))

    result = []
    cnt = defaultdict(int)
    
    for a in A:
        cnt[a] += 1
    
    for b in B:
        result.append(cnt[b])
    
    print(*result)

if __name__ == "__main__":
    main()
