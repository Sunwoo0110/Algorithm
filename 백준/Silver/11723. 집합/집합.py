import sys

def main():
    input = sys.stdin.readline
    
    n = int(input())
    mask = 0
    
    
    for _ in range(n):
        arr = input().split()
        op = arr[0]
        
        if op == "add":
            x = int(arr[1])
            mask |= (1<<(x-1))
        
        elif op == "remove":
            x = int(arr[1])
            mask &= ~(1<<(x-1))
            
        elif op == "check":
            x = int(arr[1])
            print(1 if mask&(1<<(x-1)) else 0)
        
        elif op == "toggle":
            x = int(arr[1])
            mask ^= (1<<(x-1))
        
        elif op == "all":
            mask = (1<<20)-1
        
        else:
            mask = 0
        
            
if __name__ == "__main__":
    main()