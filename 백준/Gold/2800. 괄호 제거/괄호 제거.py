import sys

def main():
    input = sys.stdin.readline
    
    st = input().strip()
    result = set()
    
    stack = []
    idx_arr = []
    
    for i in range(len(st)):
        if st[i] == "(":
            stack.append(i)
        elif st[i] == ")":
            idx_arr.append([stack[-1], i])
            stack.pop()
    
    l = len(idx_arr)
    path = [False] * l
    
    def dfs(node):
        nonlocal result
        
        if node == l:
            if not any(path):
                return
            
            remove_idx = [False] * len(st)
            for i, isUsed in enumerate(path):
                if isUsed:
                    s, e = idx_arr[i]
                    remove_idx[s] = True
                    remove_idx[e] = True
            
            res = []
            for i, ch in enumerate(st):
                if not remove_idx[i]:
                    res.append(ch)
            
            result.add(''.join(res))
            return
        
        s, e = idx_arr[node]
        
        path[node] = False
        dfs(node+1)
        path[node] = True
        dfs(node+1)
    
    dfs(0)
    answer = sorted(list(result))
    
    for ans in answer:
        print(ans)
    
if __name__ == "__main__":
    main()
