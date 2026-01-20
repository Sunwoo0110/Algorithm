import sys

def main():
    input = sys.stdin.readline
    
    s = input().strip()
    
    if s == s[::-1]:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()
