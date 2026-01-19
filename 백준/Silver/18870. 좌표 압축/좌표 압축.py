import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))
    
    sorted_arr = sorted(list(set(arr)))
    idx_dict = {}
    
    for i, num in enumerate(sorted_arr):
        idx_dict[num] = i
    
    result = []
    for a in arr:
        result.append(idx_dict[a])
    
    print(*result)

if __name__ == "__main__":
    main()
