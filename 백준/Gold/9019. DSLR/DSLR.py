import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    T = int(input())
    result = []
    
    for _ in range(T):
        A, B = map(int, input().split())
        
        queue = deque()
        queue.append(A)
        
        prev = [-1 for _ in range(10000)]
        op = ["" for _ in range(10000)]
        
        prev[A] = A
        
        while queue:
            node = queue.popleft()
            
            if node == B:
                break
            
            ## D
            nxt = node*2 if node*2 < 10000 else (node*2)%10000
            if prev[nxt] == -1:
                prev[nxt] = node
                op[nxt] = "D"
                queue.append(nxt)
                
            ## S
            nxt = node-1 if node-1 >= 0 else 9999
            if prev[nxt] == -1:
                prev[nxt] = node
                op[nxt] = "S"
                queue.append(nxt)
            
            ## L
            nxt = (node%1000)*10 + node//1000
            if prev[nxt] == -1:
                prev[nxt] = node
                op[nxt] = "L"
                queue.append(nxt)
            
            ## R
            nxt = (node%10)*1000 + node//10
            if prev[nxt] == -1:
                prev[nxt] = node
                op[nxt] = "R"
                queue.append(nxt)
        
        cur = B
        answer = []
        while cur != A:
            answer.append(op[cur])
            cur = prev[cur]
        
        answer.reverse()
        result.append(''.join(answer))
    
    print("\n".join(result))
    
    
if __name__ == "__main__":
    main()
