import sys
from collections import deque
import heapq

def main():
    input = sys.stdin.readline
    
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        
        arr = []
        for _ in range(n):
            arr.append(input().strip())

        arr.sort()
        
        ok = True
        for i in range(n-1):
            if len(arr[i]) <= len(arr[i+1]) and arr[i] == arr[i+1][:len(arr[i])]:
                ok = False
                break
        
        print("YES" if ok else "NO")

        
        

if __name__ == "__main__":
    main()