import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    
    p, m = map(int, input().split())
    
    players = defaultdict(int)
    rooms = defaultdict(list) ## key: 첫 플레이어 닉네임
    
    for _ in range(p):
        l, n = input().split()
        l = int(l)
        
        players[n] = l
        
        WasCreated = False
        for k, v in rooms.items():
            if players[k]-10 <= l <= players[k]+10 and len(rooms[k]) < m:
                rooms[k].append(n)
                WasCreated = True
                break
        
        if not WasCreated:
            rooms[n].append(n)
    
    for k, v in rooms.items():
        if len(v) == m:
            print("Started!")
        else:
            print("Waiting!")
        
        arr = v
        arr.sort()
        for a in arr:
            print(f"{players[a]} {a}")
            
if __name__ == "__main__":
    main()
