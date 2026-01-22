import sys

def main():
    input = sys.stdin.readline
    
    tc_num = int(input())
    
    for _ in range(tc_num):
        n, m = map(int, input().split())
        
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        
        A.sort()
        B.sort()
        
        cnt = 0
        j = 0 
        
        for a in A:
            while j < m and B[j] < a:
                j += 1
            cnt += j
        
        print(cnt)

if __name__ == "__main__":
    main()
