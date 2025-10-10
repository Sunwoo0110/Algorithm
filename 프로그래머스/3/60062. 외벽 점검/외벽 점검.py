def solution(n, weak, dist):
    answer = len(dist) + 1
    weak_len = len(weak)
    
    ## 반시계 방향용 (좌표 반전 + 정렬)
    weak_rev = sorted([(n-w) % n for w in weak])
    weak_rev = weak_rev + [w+n for w in weak_rev]
    
    ## 시계 방향용 (선형화)
    weak = weak + [w + n for w in weak]

    visited = [False] * len(dist)
    friends = []
    
    ## DFS: 친구 순서 정하기
    def dfs(depth):
        nonlocal answer
        if depth == len(dist):
            check(friends, weak)
            check(friends, weak_rev)
            return
        
        for i in range(len(dist)):
            if not visited[i]:
                visited[i] = True
                friends.append(dist[i])
                dfs(depth+1)
                friends.pop()
                visited[i] = False
    
    ## 현재 friends 순서로 점검 가능한지 확인
    def check(friends_order, weak_arr):
        nonlocal answer
        
        for start in range(weak_len):
            friend_idx = 0
            limit = weak_arr[start] + friends_order[friend_idx] ## 현재 커버 가능한 약점 범위
            success = True

            for idx in range(start, start+weak_len):
                if weak_arr[idx] > limit:
                    friend_idx += 1
                    if friend_idx >= len(friends_order):
                        success = False
                        break
                    limit = weak_arr[idx] + friends_order[friend_idx]
            
            if success:
                answer = min(answer, friend_idx+1)
    
    dfs(0)
    return -1 if answer > len(dist) else answer
