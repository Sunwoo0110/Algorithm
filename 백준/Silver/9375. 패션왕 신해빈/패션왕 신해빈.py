import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    T = int(input())
    
    for _ in range(T):
        n = int(input())
        
        clothes_dict = defaultdict(int)
        
        for _ in range(n):
            name, ctg = input().split()
            
            clothes_dict[ctg] += 1
        
        answer = 1
        for k, v in clothes_dict.items():
            answer *= (v+1)
        
        answer -= 1
        print(answer)
                
                    
    
if __name__ == "__main__":
    main()
