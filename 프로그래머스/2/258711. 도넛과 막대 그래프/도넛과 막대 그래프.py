from collections import defaultdict

def solution(edges):
    indeg = defaultdict(int)
    outdeg = defaultdict(int)
    graph = defaultdict(list)

    # indegree / outdegree 계산
    for a, b in edges:
        outdeg[a] += 1
        indeg[b] += 1
        graph[a].append(b)

    # 1) 생성된 정점 찾기
    created = -1
    for node in outdeg:
        if outdeg[node] >= 2 and indeg[node] == 0:
            created = node
            break

    donut, stick, eight = 0, 0, 0

    # 2) 생성 정점에서 뻗은 그래프 분류
    for nxt in graph[created]:
        cur = nxt
        visited = set()
        while True:
            if cur in visited:     # 사이클 발견 -> 도넛
                donut += 1
                break
            visited.add(cur)
            
            if outdeg[cur] == 0:   # 끝남 -> 막대
                stick += 1
                break
                
            if outdeg[cur] == 2:   # 분기 -> 8자
                eight += 1
                break

            # outdeg[cur] == 1 -> 다음 노드로 이동
            cur = graph[cur][0]

    return [created, donut, stick, eight]
