import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    
    freq_cnt = defaultdict(int)
    
    for a in arr:
        freq_cnt[a] += 1
    
    sorted_freq = sorted(freq_cnt.items(), key=lambda x: -x[1])
    result = []
    for num, cnt in sorted_freq:
        result.extend([num]*cnt)
    
    print(*result)

if __name__ == "__main__":
    main()