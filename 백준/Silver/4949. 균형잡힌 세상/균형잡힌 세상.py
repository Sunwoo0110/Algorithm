import sys
import heapq

def main():
    input = sys.stdin.readline
    
    while True:
        st = input().rstrip()
        
        if st == ".":
            break
        
        stack = []
        isBalanced = True
        
        for s in st:
            if s == "(" or s == "[":
                stack.append(s)
            elif s == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    isBalanced = False
                    break
            elif s == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    isBalanced = False
                    break
        
        if isBalanced and not stack:
            print("yes")
        else:
            print("no")
    
if __name__ == "__main__":
    main()
