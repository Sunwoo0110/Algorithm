import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    N, d, k, c = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    
    arr *= 2
    curr_dict = defaultdict(int)
    answer = 0
    
    for i in range(k):
        curr_dict[arr[i]] += 1
        
    if c not in curr_dict.keys():
        answer = len(curr_dict.keys()) + 1
    else:
        answer = len(curr_dict.keys())
    
    for i in range(N):
        if curr_dict[arr[i]] > 1:
            curr_dict[arr[i]] -= 1
        else:
            del curr_dict[arr[i]]
            
        curr_dict[arr[i+k]] += 1
        
        if c not in curr_dict.keys():
            answer = max(answer, len(curr_dict.keys())+1)
        else:
            answer = max(answer, len(curr_dict.keys()))
        
    print(answer)
            
if __name__ == "__main__":
    main()
