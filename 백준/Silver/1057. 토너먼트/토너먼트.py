import sys

def main():
    input = sys.stdin.readline
    
    n, a, b = map(int, input().split())
    round = 1
    
    while n > 1:
        if (a%2 == 1 and a+1 == b) or (a%2 == 0 and a-1 == b):
            print(round)
            return round
        
        if a%2 == 0:
            a //= 2
        else:
            a = a//2+1
        
        if b%2 == 0:
            b //= 2
        else:
            b = b//2+1
            
        round += 1
        
        if n%2 == 0:
            n //= 2
        else:
            n = n//2+1
        
    
    print(-1)
    return -1
                
            
            

if __name__ == "__main__":
    main()