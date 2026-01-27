import sys

def main():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    for i in range(n):
        for j in range(n-1):
            arr[i][j+1] += arr[i][j]
            
    for i in range(n-1):
        for j in range(n):
            arr[i+1][j] += arr[i][j]
    
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        
        result = arr[x2][y2]
        
        if x1 > 0:
            result -= arr[x1-1][y2]
            
        if y1 > 0:
            result -= arr[x2][y1-1]
            
        if x1 > 0 and y1 > 0:
            result += arr[x1-1][y1-1]
        
        print(result)
            
        
    
            
if __name__ == "__main__":
    main()
