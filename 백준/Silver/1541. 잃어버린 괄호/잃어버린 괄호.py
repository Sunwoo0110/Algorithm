import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    s = input().strip()
    stack = []
    
    n = len(s)
    idx = 0
        
    minus_mode = False
    
    while idx < n:
        
        num = ""
        while idx < n and s[idx].isdigit():
            num += s[idx]
            idx += 1
        num = int(num)
        
        if minus_mode:
            stack.append(-num)
        else:
            stack.append(num)

        
        if idx < n:
            if s[idx] == "-":
                minus_mode = True
            idx += 1
        
    print(sum(stack))
            
if __name__ == "__main__":
    main()
