import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    k, l = map(int, input().split())
    
    num_dict = defaultdict(int)
    
    for i in range(l):
        num =  input().strip()
        
        num_dict[num] = i
    
    sorted_num_dict = sorted(num_dict.items(), key=lambda x: x[1])
    
    for i in range(min(k, len(sorted_num_dict))):
        print(sorted_num_dict[i][0])
            

if __name__ == "__main__":
    main()