import sys

def main():
    input = sys.stdin.readline
    
    n = int(input())
    m = int(input())
    num_set = set(list(map(int, input().split())))
    answer = 0
    
    for num in num_set:
        if num*2 != m and (m-num) in num_set:
            answer += 1
    
    print(answer//2)
    
    
if __name__ == "__main__":
    main()