import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    
    arrA, arrB = arr[:n//2], arr[n//2:]
    lA, lB = len(arrA), len(arrB)
    sumA, sumB = [], []
    
    def dfs(idx, total, type): 
        
        if idx == lA and type == "A":
            sumA.append(total)
            return
        if idx == lB and type == "B":
            sumB.append(total)
            return
        
        if type == "A":
            dfs(idx+1, total+arrA[idx], type)
        else:
            dfs(idx+1, total+arrB[idx], type)
        dfs(idx+1, total, type)
    
    dfs(0, 0, "A")
    dfs(0, 0, "B")
    
    sumA.sort()
    sumB.sort()
    answer = 0
    
    left, right = 0, len(sumB)-1
    
    while left < len(sumA) and right >= 0:
        if sumA[left] + sumB[right] <= c:
            answer += (right+1)
            left += 1
        else:
            right -= 1
    
    print(answer)
    
if __name__ == "__main__":
    main()
