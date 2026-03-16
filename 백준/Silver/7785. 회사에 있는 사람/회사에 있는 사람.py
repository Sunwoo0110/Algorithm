import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    n = int(input())
    
    employee_set = set()
    
    for _ in range(n):
        name, typ = input().split()
        
        if typ == "enter":
            employee_set.add(name)
        else:
            employee_set.remove(name)
    
    employee_arr = list(employee_set)
    employee_arr.sort(reverse=True)
    
    for e in employee_arr:
        print(e)
    
if __name__ == "__main__":
    main()