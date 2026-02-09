import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    T = int(input())
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))
    
    prefix_A = [0]*(n+1)
    prefix_B = [0]*(m+1)
    
    for i in range(n):
        prefix_A[i+1] = prefix_A[i] + A[i]
    for j in range(m):
        prefix_B[j+1] = prefix_B[j] + B[j]
    
    def sub_sums(prefix):
        l = len(prefix)
        sums = []
        for i in range(l-1):
            for j in range(i, l-1):
                sums.append(prefix[j+1]-prefix[i])
        return sums

    sums_A = sub_sums(prefix_A)
    sums_B = sub_sums(prefix_B)
    
    cnt_B = defaultdict(int)
    for b in sums_B:
        cnt_B[b] += 1
    
    answer = 0
    for a in sums_A:
        answer += cnt_B[T-a]
    
    print(answer)
    
            
if __name__ == "__main__":
    main()
