from collections import deque

def solution(n, m, x, y, r, c, k):
    answer = ''
    x, y, r, c = x-1, y-1, r-1, c-1

    stack = [(x, y, [], 0)]
    
    while stack:
        dx, dy, path, l = stack.pop()

        if answer:
            break

        dist = abs(dx - r) + abs(dy - c)
        remain = k - l
        if dist > remain or (remain - dist) % 2 != 0:
            continue

        if l == k:
            if (dx, dy) == (r, c):
                answer = ''.join(path)
                break
            continue
        
        ## 역순
        if 0 <= dx-1 < n:
            stack.append((dx-1, dy, path+["u"], l+1))
        if 0 <= dy+1 < m:
            stack.append((dx, dy+1, path+["r"], l+1))
        if 0 <= dy-1 < m:
            stack.append((dx, dy-1, path+["l"], l+1))
        if 0 <= dx+1 < n:
            stack.append((dx+1, dy, path+["d"], l+1))
    
    return answer if answer else "impossible"

