import sys

def main():
    input = sys.stdin.readline

    n, m = map(int, input().strip().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = []
    
    i, j = 0, 0
    
    while i < n and j < m:
        if A[i] < B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1

    while i < n:
        result.append(A[i])
        i += 1

    while j < m:
        result.append(B[j])
        j += 1
    
    print(*result)

if __name__ == "__main__":
    main()
