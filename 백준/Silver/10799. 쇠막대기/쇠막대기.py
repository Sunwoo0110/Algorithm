import sys

def main():
    input = sys.stdin.readline
    
    exp = input().strip()
    l = len(exp)
    stack = []
    answer = 0
    
    for i in range(l):
        s = exp[i]
        if s == "(":
            stack.append(s)
        else:
            if exp[i-1] == "(":
                stack.pop()
                answer += len(stack)
            else:
                stack.pop()
                answer += 1
    print(answer)
    
if __name__ == "__main__":
    main()
