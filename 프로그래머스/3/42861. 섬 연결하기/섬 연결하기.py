def solution(n, costs):
    answer = 0
    
    parent = [i for i in range(n)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x]) ## 경로 압축
        return parent[x]
    
    
    ## 합집합
    def union(a, b):
        a_root = find(a)
        b_root = find(b)
        
        if a_root != b_root:
            parent[b_root] = a_root
            return True
        
        ## 이미 같은 그룹
        return False
    
    ## 비용 낮은 순으로
    costs.sort(key=lambda x: x[2])
    
    edge_cnt = 0
    
    for a, b, cost in costs:
        if union(a, b):
            answer += cost
            edge_cnt += 1
            
        if edge_cnt == n-1:
            break
    
    
    return answer