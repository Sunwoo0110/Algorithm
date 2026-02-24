import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    pass_map = defaultdict(str)
    
    for _ in range(n):
        site, pw = input().split()
        pass_map[site] = pw
        
    for _ in range(m):
        site = input().strip()
        print(pass_map[site])
    
if __name__ == "__main__":
    main()
