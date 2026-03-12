import sys

def main():
    input = sys.stdin.readline
    
    n = int(input())
    
    arr = [0 for _ in range(9)]
    
    n = str(n)
    
    for num in n:
        a = int(num)
        
        if a == 9:
            arr[6] += 1
        else:
            arr[a] += 1
    
    arr[6] = (arr[6]+1) // 2
    print(max(arr))
    
if __name__ == "__main__":
    main()