import sys

def main():
    input = sys.stdin.readline
    
    arr = []
    for _ in range(4):
        arr.append(list(map(int, input().strip())))
        
    k = int(input())
    
    top_idx = [0, 0, 0, 0]
    
    for _ in range(k):
        n, d = map(int, input().split())
        left, right, cur_d = n-2, n, d*(-1)
        prev = top_idx[:]
        top_idx[n-1] = (top_idx[n-1]-d+8)%8
        
        ## 왼쪽
        while left >= 0:
            if arr[left][(prev[left]+2)%8] != arr[left+1][(prev[left+1]+6)%8]:
                top_idx[left] = (prev[left]-cur_d+8)%8
            else:
                break
            
            left -= 1
            cur_d *= -1
        
        cur_d = d*(-1)
        ## 오른쪽
        while right < 4:
            if arr[right][(prev[right]+6)%8] != arr[right-1][(prev[right-1]+2)%8]:
                top_idx[right] = (prev[right]-cur_d+8)%8
            else:
                break
            
            right += 1
            cur_d *= -1
            
    
    result = 0
    for i in range(4):
        if arr[i][top_idx[i]] == 1:
            result += 2**i
    
    print(result)

if __name__ == "__main__":
    main()
