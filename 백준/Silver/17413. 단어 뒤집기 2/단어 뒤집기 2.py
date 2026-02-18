import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    str = input().strip()
    isTag = False
    answer = []
    tmp = ""
    
    for s in str:
        if s == "<":
            isTag = True
            answer.extend(tmp[::-1])
            tmp = ""
        elif s == ">":
            isTag = False
            tmp = ""
            answer.append(s)
            continue
        
        if isTag:
            answer.append(s)
        else:
            if s == " ":
                answer.extend(tmp[::-1])
                answer.append(" ")
                tmp = ""
            else:
                tmp += s
    answer.extend(tmp[::-1])
    print(''.join(answer))
    
    
if __name__ == "__main__":
    main()
