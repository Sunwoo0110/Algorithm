def solution(user_id, banned_id):
    answer_set = set()

    def is_match(user, ban):
        if len(user) != len(ban):
            return False
        for u, b in zip(user, ban):
            if b != '*' and u != b:
                return False
        return True
    
    candidates = []
    for ban in banned_id:
        can = []
        for user in user_id:
            if is_match(user, ban):
                can.append(user)
        candidates.append(can)

    def dfs(depth, path):
        if depth == len(candidates):
            answer_set.add(frozenset(path))
            return
        for user in candidates[depth]:
            if user not in path:
                dfs(depth+1, path+[user])

    dfs(0, [])
    
    return len(answer_set)
