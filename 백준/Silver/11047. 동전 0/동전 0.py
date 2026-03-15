import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    n, k = map(int, input().split())
    coins = []
    
    for _ in range(n):
        coins.append(int(input()))
    
    answer = 0
    
    for coin in coins[::-1]:
        if coin > k:
            continue
        
        answer += k//coin
        k = k-(k//coin)*coin
        
        if k == 0:
            break
    
    print(answer)
    
    
if __name__ == "__main__":
    main()
