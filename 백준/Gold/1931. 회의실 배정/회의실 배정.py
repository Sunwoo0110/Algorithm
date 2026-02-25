import sys
import heapq

def main():
    input = sys.stdin.readline
    
    n = int(input())
    arr = []
    
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    arr.sort(key=lambda x: (x[1], x[0]))
    
    answer = 0
    prev = -1
    for s, e in arr:
        if prev <= s:
            answer += 1
            prev = e
    
    print(answer)
    
if __name__ == "__main__":
    main()