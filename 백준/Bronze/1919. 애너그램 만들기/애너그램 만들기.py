import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    s1 = input().strip()
    s2 = input().strip()
    
    s1_dict = defaultdict(int)
    s2_dict = defaultdict(int)
    
    for i in s1:
        s1_dict[i] += 1
    for j in s2:
        s2_dict[j] += 1
    
    answer = 0
    for ch1 in s1_dict.keys():
        if ch1 not in s2_dict.keys():
            answer += s1_dict[ch1]
        else:
            answer += abs(s1_dict[ch1]-s2_dict[ch1])
    for ch2 in s2_dict.keys():
        if ch2 not in s1_dict.keys():
            answer += s2_dict[ch2]
    
    print(answer)
            
if __name__ == "__main__":
    main()