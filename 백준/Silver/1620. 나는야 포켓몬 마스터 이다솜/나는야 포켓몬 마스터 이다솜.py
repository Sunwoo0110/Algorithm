import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    
    name_num_dict = defaultdict(int)
    num_name_dict = defaultdict(str)
    idx = 1
    
    for _ in range(n):
        name = input().strip()
        name_num_dict[name] = idx
        num_name_dict[idx] = name
        idx += 1
    
    for _ in range(m):
        inp = input().strip()
        
        if inp.isdigit():
            inp = int(inp)
            print(num_name_dict[inp])
        else:
            print(name_num_dict[inp])
        
    
    
    
if __name__ == "__main__":
    main()
