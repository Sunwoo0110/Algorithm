import sys
from collections import deque

def main():
    input = sys.stdin.readline
    
    T = int(input())
    
    for _ in range(T):
        p = input().strip()
        n = int(input())
        
        s = input().strip()
        arr = []
        if s != "[]":
            arr = list(map(int, s[1:-1].split(',')))
        
        d_cnt = 0
        for code in p:
            if code == "D":
                d_cnt += 1
        
        if d_cnt > n:
            print("error")
            continue
        
        isReverse = False
        queue = deque(arr)
        
        for code in p:
            if code == "R":
                isReverse = not isReverse
            else:
                if isReverse:
                    queue.pop()
                else:
                    queue.popleft()
        
        if isReverse:
            queue.reverse()
        print("[" + ",".join(map(str, queue)) + "]")
        
    
if __name__ == "__main__":
    main()
