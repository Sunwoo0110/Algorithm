import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    T = int(input())

    for _ in range(T):
        w = input().strip()
        k = int(input())

        pos = defaultdict(list)
        for i, ch in enumerate(w):
            pos[ch].append(i)

        min_len = float('inf')
        max_len = -1

        for ch in pos:
            arr = pos[ch]
            if len(arr) < k:
                continue

            for i in range(len(arr)-k+1):
                length = arr[i+k-1]-arr[i]+1
                min_len = min(min_len, length)
                max_len = max(max_len, length)

        if max_len == -1:
            print(-1)
        else:
            print(min_len, max_len)

if __name__ == "__main__":
    main()