import sys

def main():
    input = sys.stdin.readline
    
    T = int(input())
    
    for _ in range(T):
        s = input().strip()
        
        left, right = 0, len(s)-1
        
        def isPal(l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if isPal(left, right-1) or isPal(left+1, right):
                    print(1)
                else:
                    print(2)
                break
        else:
            print(0)
    
    
if __name__ == "__main__":
    main()