import sys

def main():
    input = sys.stdin.readline
    
    n = int(input())
    arr = list(map(int, input().split()))
    cal_arr = list(map(int, input().split()))
    
    max_num, min_num = -10**9, 10**9
    
    ## 백트래킹
    def dfs(idx, num):
        nonlocal cal_arr, max_num, min_num
        
        if idx == n:
            max_num = max(max_num, num)
            min_num = min(min_num, num)
            return
        
        for j in range(4):
            if cal_arr[j] > 0:
                cal_arr[j] -= 1
                
                if j == 0:
                    dfs(idx+1, num+arr[idx])
                elif j == 1:
                    dfs(idx+1, num-arr[idx])
                elif j == 2:
                    dfs(idx+1, num*arr[idx])
                else:
                    if num < 0:
                        dfs(idx+1, -(abs(num)//arr[idx]))
                    else:
                        dfs(idx+1, num//arr[idx])
                
                cal_arr[j] += 1
    
    dfs(1, arr[0])
    print(max_num)
    print(min_num)
    

if __name__ == "__main__":
    main()
