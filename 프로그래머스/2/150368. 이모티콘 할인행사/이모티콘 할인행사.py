def solution(users, emoticons):
    answer = [0, 0]
    n = len(emoticons)
    
    path = [[False for _ in range(4)] for _ in range(n)]
    dis_dict = {0: 10, 1: 20, 2: 30, 3: 40}
    
    def calc_user(path):
        plus_cnt, total_money = 0, 0
        for discount, max_money in users:
            user_money = 0
            for i in range(n):
                for j in range(4):
                    if path[i][j] and dis_dict[j] >= discount:
                        user_money += emoticons[i]*(100-dis_dict[j])/100
            if user_money >= max_money:
                plus_cnt += 1
            else:
                total_money += user_money
        
        return [plus_cnt, total_money]      
    
    def dfs(idx, path):
        nonlocal answer
        
        if idx == n-1:
            ## 이모티콘 금액, 가입 계산
            result = calc_user(path)
            if result[0] > answer[0] or (result[0] == answer[0] and result[1] > answer[1]):
                answer = result
        else:
            for nxt in range(4):
                path[idx+1][nxt] = True
                dfs(idx+1, path)
                path[idx+1][nxt] = False
    
    dfs(-1, path)
    
    return answer