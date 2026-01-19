import sys

def main():
    input = sys.stdin.readline

    n = int(input().strip())
    arr = list(map(int, input().split()))
    x = int(input().strip())

    seen = set()
    cnt = 0

    for a in arr:
        if (x-a) in seen:
            cnt += 1
        seen.add(a)

    print(cnt)

if __name__ == "__main__":
    main()