import sys
from collections import Counter

def main():
    input = sys.stdin.readline
    
    n = int(input())
    arr = []
    
    for _ in range(n):
        arr.append(int(input()))
    
    arr.sort()
    
    ## 산술평균
    avg = int(round(sum(arr)/n))
    
    ## 중앙값
    median = arr[n//2]
    
    ## 최빈값
    counter = Counter(arr)
    max_freq = max(counter.values())
    modes = [num for num, cnt in counter.items() if cnt == max_freq]
    modes.sort()
    
    if len(modes) == 1:
        mode = modes[0]
    else:
        mode = modes[1]
    
    ## 범위
    range_val = arr[-1]-arr[0]
    
    print(avg)
    print(median)
    print(mode)
    print(range_val)

if __name__ == "__main__":
    main()