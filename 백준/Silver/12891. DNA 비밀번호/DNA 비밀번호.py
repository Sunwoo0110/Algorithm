import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    s, p = map(int, input().split())
    arr = input().strip()
    a, c, g, t = map(int, input().split())
    
    curr = defaultdict(int)
    
    answer = 0
    
    for i in range(p):
        curr[arr[i]] += 1
    
    if curr["A"] >= a and curr["C"] >= c and curr["G"] >= g and curr["T"] >= t:
            answer += 1
        
    for i in range(s-p):
        curr[arr[i]] -= 1
        curr[arr[i+p]] += 1
        
        if curr["A"] >= a and curr["C"] >= c and curr["G"] >= g and curr["T"] >= t:
            answer += 1
    
    print(answer)
        
        
    
    
if __name__ == "__main__":
    main()