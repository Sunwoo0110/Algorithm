from collections import Counter

def make_combinations(arr, c):
    result = []
    
    def dfs(start, path):
        if len(path) == c:
            result.append(''.join(path))
            return
        
        for i in range(start, len(arr)):
            dfs(i+1, path+[arr[i]])
    
    dfs(0, [])
    return result


def solution(orders, course):
    answer = []
    
    for c in course:
        counter = Counter()
        
        for order in orders:
            if len(order) < c:
                continue
                
            arr = sorted(list(order))
            combs = make_combinations(arr, c)
            for comb in combs:
                counter[comb] += 1
        
        # 가장 많이 나온 조합 찾기
        if counter:
            max_cnt = max(counter.values())
            if max_cnt >= 2:
                for k, v in counter.items():
                    if v == max_cnt:
                        answer.append(k)
    
    return sorted(answer)
