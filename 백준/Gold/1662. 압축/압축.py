import sys

def main():
    input = sys.stdin.readline
    
    s = input().strip()
    
    stack = [] ## 현재까지 길이, 반복 횟수 저장
    k = int(s[0])
    
    cur = 0 ## 현재까지 길이
    
    for i in range(len(s)):
        if s[i].isdigit():
            if i+1 < len(s) and s[i+1] == "(":
                k = int(s[i])
            else:
                cur += 1
                
        elif s[i] == "(":
            stack.append((cur, k))
            cur = 0
        elif s[i] == ")":
            prev, cur_k = stack.pop()
            cur = cur*cur_k + prev
            
    print(cur)
                
            
            

if __name__ == "__main__":
    main()
