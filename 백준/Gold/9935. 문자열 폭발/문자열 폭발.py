import sys

def main():
    input = sys.stdin.readline
    
    s = input().strip()
    target = input().strip()
    
    s_len = len(s)
    target_len = len(target)
    
    stack = []
    
    for ch in s:
        stack.append(ch)
        
        if ch == target[-1] and len(stack) >= target_len:
            if ''.join(stack[-target_len:]) == target:
                del stack[-target_len:]
    
    if stack:
        print(''.join(stack))
    else:
        print("FRULA")
                
            
            

if __name__ == "__main__":
    main()
